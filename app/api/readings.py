from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.sensor_reading import SensorReading
from app.schemas.reading import ReadingIn

router = APIRouter(prefix="/readings", tags=["readings"])


@router.post("", status_code=status.HTTP_202_ACCEPTED)
def ingest_readings(readings: list[ReadingIn], db: Session = Depends(get_session)) -> dict[str, int]:
    """Batch ingestion endpoint called by the MQTT bridge."""
    for reading in readings:
        db.add(SensorReading(**reading.model_dump()))
    db.commit()
    return {"accepted": len(readings)}
