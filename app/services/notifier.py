"""Excursion alerts: e-mail to the QA duty officer and an optional customer webhook."""

import logging
import smtplib
import time
from email.message import EmailMessage

import httpx

from app.config import settings

log = logging.getLogger(__name__)
WEBHOOK_ATTEMPTS = 4


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


def notify_excursion(shipment_ref: str, peak_c: float, qa_email: str, webhook_url: str | None) -> None:
    subject = f"[EXCURSION] {shipment_ref} peaked at {peak_c:.1f} C"
    send_email(qa_email, subject, f"Shipment {shipment_ref} has been quarantined pending QA review.")
    if webhook_url:
        send_webhook(webhook_url, {"event": "excursion", "shipment": shipment_ref, "peak_c": peak_c})
