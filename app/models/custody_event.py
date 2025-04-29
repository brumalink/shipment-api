from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class CustodyEvent(Base):
    """A handover of a shipment between parties (warehouse, driver, carrier, pharmacy).

    Events are append-only. `hash` chains each event to the previous one for the same shipment,
    so any later modification of the history is detectable (see ADR 0003).
    """

    __tablename__ = "custody_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    shipment_id: Mapped[int] = mapped_column(ForeignKey("shipments.id"), index=True)
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    from_party: Mapped[str] = mapped_column(String(64))
    to_party: Mapped[str] = mapped_column(String(64))
    location: Mapped[str] = mapped_column(String(64))
    signed_by: Mapped[str] = mapped_column(String(64))
    prev_hash: Mapped[str] = mapped_column(String(64))
    hash: Mapped[str] = mapped_column(String(64), unique=True)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
