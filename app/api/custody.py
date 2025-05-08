from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.custody_event import CustodyEvent
from app.models.shipment import Shipment
from app.services.custody_hash import verify_chain

router = APIRouter(prefix="/shipments", tags=["custody"])


@router.get("/{reference}/custody")
def custody_chain(reference: str, db: Session = Depends(get_session)) -> dict:
    shipment = db.scalar(select(Shipment).where(Shipment.reference == reference))
    if shipment is None:
        raise HTTPException(404, "Shipment not found")

    events = db.scalars(
        select(CustodyEvent).where(CustodyEvent.shipment_id == shipment.id).order_by(CustodyEvent.id)
    ).all()
    payloads = [
        {
            "occurred_at": e.occurred_at.isoformat(),
            "from": e.from_party,
            "to": e.to_party,
            "location": e.location,
            "signed_by": e.signed_by,
        }
        for e in events
    ]
    broken_at = verify_chain(payloads, [e.hash for e in events])
    return {"reference": reference, "events": payloads, "intact": broken_at is None, "broken_at": broken_at}
