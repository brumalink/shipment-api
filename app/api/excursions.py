from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.sensor_reading import SensorReading
from app.models.shipment import Shipment
from app.services import excursion_detector

router = APIRouter(prefix="/shipments", tags=["excursions"])


@router.get("/{reference}/excursions")
def list_excursions(reference: str, db: Session = Depends(get_session)) -> list[dict]:
    shipment = db.scalar(select(Shipment).where(Shipment.reference == reference))
    if shipment is None:
        raise HTTPException(404, "Shipment not found")
    if shipment.tracker_id is None:
        return []

    rows = db.scalars(
        select(SensorReading)
        .where(SensorReading.tracker_id == shipment.tracker_id)
        .where(SensorReading.recorded_at >= shipment.created_at)
    ).all()
    readings = [excursion_detector.Reading(r.recorded_at, r.temperature_c) for r in rows]
    return [
        {"started_at": e.started_at, "ended_at": e.ended_at, "peak_c": e.peak_c}
        for e in excursion_detector.detect(readings, profile=shipment.product_profile)
    ]
