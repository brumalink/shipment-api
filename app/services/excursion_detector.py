"""Temperature excursion detection.

An excursion is a continuous run of readings outside the allowed temperature range.
"""

from dataclasses import dataclass
from datetime import datetime

MIN_TEMP_C = 2.0
MAX_TEMP_C = 8.0


@dataclass(frozen=True)
class Reading:
    recorded_at: datetime
    temperature_c: float


@dataclass(frozen=True)
class Excursion:
    started_at: datetime
    ended_at: datetime
    peak_c: float


def _outside(temp: float) -> bool:
    return temp < MIN_TEMP_C or temp > MAX_TEMP_C


def detect(readings: list[Reading]) -> list[Excursion]:
    excursions: list[Excursion] = []
    run: list[Reading] = []
    for reading in sorted(readings, key=lambda r: r.recorded_at):
        if _outside(reading.temperature_c):
            run.append(reading)
            continue
        if run:
            excursions.append(_to_excursion(run))
            run = []
    if run:
        excursions.append(_to_excursion(run))
    return excursions


def _to_excursion(run: list[Reading]) -> Excursion:
    peak = max(run, key=lambda r: abs(r.temperature_c - (MIN_TEMP_C + MAX_TEMP_C) / 2))
    return Excursion(run[0].recorded_at, run[-1].recorded_at, peak.temperature_c)
