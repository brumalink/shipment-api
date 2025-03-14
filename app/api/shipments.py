from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.shipment import Shipment
from app.schemas.shipment import ShipmentCreate, ShipmentOut

router = APIRouter(prefix="/shipments", tags=["shipments"])

PROFILE_LIMITS = {"2-8C": (2.0, 8.0), "15-25C": (15.0, 25.0), "frozen": (-25.0, -15.0)}


@router.post("", response_model=ShipmentOut, status_code=status.HTTP_201_CREATED)
def create_shipment(payload: ShipmentCreate, db: Session = Depends(get_session)):
    if payload.product_profile not in PROFILE_LIMITS:
        raise HTTPException(422, f"Unknown product profile {payload.product_profile!r}")
    low, high = PROFILE_LIMITS[payload.product_profile]
    shipment = Shipment(**payload.model_dump(), min_temp_c=low, max_temp_c=high)
    db.add(shipment)
    db.commit()
    db.refresh(shipment)
    return shipment


@router.get("", response_model=list[ShipmentOut])
def list_shipments(db: Session = Depends(get_session)):
    return db.scalars(select(Shipment).order_by(Shipment.created_at.desc())).all()


@router.get("/{reference}", response_model=ShipmentOut)
def get_shipment(reference: str, db: Session = Depends(get_session)):
    shipment = db.scalar(select(Shipment).where(Shipment.reference == reference))
    if shipment is None:
        raise HTTPException(404, "Shipment not found")
    return shipment
