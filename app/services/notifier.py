"""Excursion alerts: e-mail to the QA duty officer and an optional customer webhook."""

import logging
import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

import httpx

from app.config import settings

log = logging.getLogger(__name__)
WEBHOOK_ATTEMPTS = 4

# (shipment, excursion start) pairs already alerted. Trackers re-send buffered readings after
# reconnecting, which used to re-trigger the same excursion and page the QA officer twice.
_alerted: set[tuple[str, datetime]] = set()


def send_email(to: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = settings.alert_email_from
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP(settings.alert_smtp_host) as smtp:
        smtp.send_message(msg)


def send_webhook(url: str, payload: dict) -> None:
    """POST with exponential backoff (1s, 2s, 4s) - customer endpoints are often flaky."""
    for attempt in range(1, WEBHOOK_ATTEMPTS + 1):
        try:
            httpx.post(url, json=payload, timeout=settings.alert_webhook_timeout_s).raise_for_status()
            return
        except httpx.HTTPError as exc:
            if attempt == WEBHOOK_ATTEMPTS:
                raise
            log.warning("Webhook %s failed (attempt %d): %s", url, attempt, exc)
            time.sleep(2 ** (attempt - 1))


def notify_excursion(
    shipment_ref: str, started_at: datetime, peak_c: float, qa_email: str, webhook_url: str | None
) -> bool:
    """Send alerts once per excursion. Returns False if this excursion was already alerted."""
    key = (shipment_ref, started_at)
    if key in _alerted:
        return False
    _alerted.add(key)

    subject = f"[EXCURSION] {shipment_ref} peaked at {peak_c:.1f} C"
    send_email(qa_email, subject, f"Shipment {shipment_ref} has been quarantined pending QA review.")
    if webhook_url:
        payload = {"event": "excursion", "shipment": shipment_ref, "started_at": started_at.isoformat(),
                   "peak_c": peak_c}
        send_webhook(webhook_url, payload)
    return True
