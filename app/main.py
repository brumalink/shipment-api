from fastapi import FastAPI

from app import __version__
from app.api import custody, excursions, health, readings, shipments, tenants

app = FastAPI(
    title="Brumalink Shipment API",
    version=__version__,
    description="Shipments, tracker readings, temperature excursions and chain of custody.",
)
app.include_router(health.router)
app.include_router(shipments.router)
app.include_router(readings.router)
app.include_router(excursions.router)
app.include_router(custody.router)
app.include_router(tenants.router)
