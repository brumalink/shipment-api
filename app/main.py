from fastapi import FastAPI

from app import __version__
from app.api import shipments

app = FastAPI(title="Brumalink Shipment API", version=__version__)
app.include_router(shipments.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
