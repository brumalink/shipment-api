from datetime import datetime

from pydantic import BaseModel, Field


class ReadingIn(BaseModel):
    tracker_id: str = Field(examples=["BLT3-00F1A2"])
    sequence: int = Field(ge=0, description="Monotonic per tracker, resets only on factory reset")
    recorded_at: datetime
    temperature_c: float = Field(ge=-80, le=80)
    humidity_pct: float | None = Field(default=None, ge=0, le=100)
    battery_pct: int | None = Field(default=None, ge=0, le=100)
