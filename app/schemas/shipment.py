from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models.shipment import ShipmentStatus


class ShipmentCreate(BaseModel):
    reference: str = Field(pattern=r"^BL-\d{4}-\d{6}$", examples=["BL-2025-000123"])
    product_profile: str = Field(examples=["2-8C"])
    origin: str = Field(examples=["WAW-HUB-1"])
    destination: str = Field(examples=["Apteka Centralna, Poznan"])
    tracker_id: str | None = Field(default=None, examples=["BLT3-00F1A2"])


class ShipmentOut(ShipmentCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: ShipmentStatus
    min_temp_c: float
    max_temp_c: float
    created_at: datetime
