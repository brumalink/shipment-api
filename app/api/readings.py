import hashlib
import hmac

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from sqlalchemy import select, tuple_
from sqlalchemy.orm import Session

from app.config import settings
from app.db import get_session
from app.models.sensor_reading import SensorReading
from app.schemas.reading import ReadingIn

router = APIRouter(prefix="/readings", tags=["readings"])


async def verify_signature(request: Request, x_tracker_signature: str = Header()) -> None:
    """Reject payloads not signed by the MQTT bridge (HMAC-SHA256 over the raw body, hex encoded)."""
    body = await request.body()
    expected = hmac.new(settings.tracker_shared_secret.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, x_tracker_signature.strip().lower()):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid tracker signature")


@router.post("", status_code=status.HTTP_202_ACCEPTED, dependencies=[Depends(verify_signature)])
def ingest_readings(readings: list[ReadingIn], db: Session = Depends(get_session)) -> dict[str, int]:
    """Batch ingestion endpoint called by the MQTT bridge.

    Trackers re-send their buffer after reconnecting, so the same (tracker_id, sequence)
    can arrive more than once - duplicates are skipped, not stored twice.
    """
    keys = {(r.tracker_id, r.sequence) for r in readings}
    existing = set(
        db.execute(
            select(SensorReading.tracker_id, SensorReading.sequence).where(
                tuple_(SensorReading.tracker_id, SensorReading.sequence).in_(keys)
            )
        ).all()
    )
    fresh = {(r.tracker_id, r.sequence): r for r in readings if (r.tracker_id, r.sequence) not in existing}
    db.add_all(SensorReading(**r.model_dump()) for r in fresh.values())
    db.commit()
    return {"accepted": len(fresh), "duplicates": len(readings) - len(fresh)}
