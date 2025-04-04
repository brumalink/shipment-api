from fastapi import FastAPI

from app import __version__
from app.api import health, readings, shipments

app = FastAPI(title="Brumalink Shipment API", version=__version__)
app.include_router(health.router)
app.include_router(shipments.router)
app.include_router(readings.router)
