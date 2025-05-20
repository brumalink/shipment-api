"""Temperature excursion detection.

An excursion is a continuous run of readings outside the product's temperature profile.
Profiles follow the labelled storage conditions agreed with our pharma customers (ADR 0002).
"""

from dataclasses import dataclass
from datetime import datetime

PROFILES: dict[str, tuple[float, float]] = {
    "2-8C": (2.0, 8.0),  # vaccines, insulin, biologics
    "15-25C": (15.0, 25.0),  # controlled room temperature
    "frozen": (-25.0, -15.0),  # frozen plasma, some diagnostics
}


@dataclass(frozen=True)
class Reading:
    recorded_at: datetime
    temperature_c: float


@dataclass(frozen=True)
class Excursion:
    started_at: datetime
    ended_at: datetime
    peak_c: float


def _deviation(temp: float, low: float, high: float) -> float:
    if temp < low:
        return low - temp
    if temp > high:
        return temp - high
    return 0.0


def detect(readings: list[Reading], profile: str = "2-8C") -> list[Excursion]:
    try:
        low, high = PROFILES[profile]
    except KeyError:
        raise ValueError(f"Unknown product profile: {profile!r}") from None

    excursions: list[Excursion] = []
    run: list[Reading] = []
    for reading in sorted(readings, key=lambda r: r.recorded_at):
        if _deviation(reading.temperature_c, low, high) > 0:
            run.append(reading)
            continue
        if run:
            excursions.append(_to_excursion(run, low, high))
            run = []
    if run:
        excursions.append(_to_excursion(run, low, high))
    return excursions


def _to_excursion(run: list[Reading], low: float, high: float) -> Excursion:
    worst = max(run, key=lambda r: _deviation(r.temperature_c, low, high))
    return Excursion(run[0].recorded_at, run[-1].recorded_at, worst.temperature_c)
