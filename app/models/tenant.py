import re

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]{2,30}[a-z0-9]$")
DATA_REGIONS = {"eu-central", "eu-north"}


def validate_slug(slug: str) -> str:
    """Tenant slugs appear in URLs and object-storage prefixes, so keep them boring."""
    if not SLUG_RE.fullmatch(slug) or "--" in slug:
        raise ValueError(f"Invalid tenant slug: {slug!r}")
    return slug


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(32), unique=True)
    name: Mapped[str] = mapped_column(String(128))
    data_region: Mapped[str] = mapped_column(String(16), default="eu-central")
