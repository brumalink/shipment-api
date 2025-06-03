"""Excursion alerts: e-mail to the QA duty officer and an optional customer webhook."""

import smtplib
from email.message import EmailMessage

import httpx

from app.config import settings


def send_email(to: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = settings.alert_email_from
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP(settings.alert_smtp_host) as smtp:
        smtp.send_message(msg)


def send_webhook(url: str, payload: dict) -> None:
    httpx.post(url, json=payload, timeout=settings.alert_webhook_timeout_s).raise_for_status()


def notify_excursion(shipment_ref: str, peak_c: float, qa_email: str, webhook_url: str | None) -> None:
    subject = f"[EXCURSION] {shipment_ref} peaked at {peak_c:.1f} C"
    send_email(qa_email, subject, f"Shipment {shipment_ref} has been quarantined pending QA review.")
    if webhook_url:
        send_webhook(webhook_url, {"event": "excursion", "shipment": shipment_ref, "peak_c": peak_c})
