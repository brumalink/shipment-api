from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import get_session
from app.models.tenant import DATA_REGIONS, Tenant, validate_slug

router = APIRouter(prefix="/tenants", tags=["tenants"])


class TenantIn(BaseModel):
    slug: str
    name: str
    data_region: str = "eu-central"


@router.get("")
def list_tenants(db: Session = Depends(get_session)) -> list[dict]:
    return [
        {"slug": t.slug, "name": t.name, "data_region": t.data_region}
        for t in db.scalars(select(Tenant).order_by(Tenant.slug))
    ]


@router.post("", status_code=status.HTTP_201_CREATED)
def create_tenant(payload: TenantIn, db: Session = Depends(get_session)) -> dict:
    try:
        slug = validate_slug(payload.slug)
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    if payload.data_region not in DATA_REGIONS:
        raise HTTPException(422, f"Unsupported data region {payload.data_region!r}")
    db.add(Tenant(slug=slug, name=payload.name, data_region=payload.data_region))
    db.commit()
    return {"slug": slug}
