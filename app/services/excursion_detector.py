"""Temperature excursion detection.

An excursion is a continuous run of readings outside the product's temperature profile.
Profiles follow the labelled storage conditions agreed with our pharma customers (ADR 0002).

Short spikes (door opened during loading) are tolerated per SOP-TR-07: a run shorter than
the grace period is ignored, unless it deviates from the profile by HARD_DEVIATION_C or more.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta

PROFILES: dict[str, tuple[float, float]] = {
    "2-8C": (2.0, 8.0),  # vaccines, insulin, biologics
    "15-25C": (15.0, 25.0),  # controlled room temperature
    "frozen": (-25.0, -15.0),  # frozen plasma, some diagnostics
}
DEFAULT_GRACE = timedelta(minutes=10)
HARD_DEVIATION_C = 5.0


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


def detect(
    readings: list[Reading], profile: str = "2-8C", grace: timedelta = DEFAULT_GRACE
) -> list[Excursion]:
    try:
        low, high = PROFILES[profile]
    except KeyError:
        raise ValueError(f"Unknown product profile: {profile!r}") from None

    runs: list[list[Reading]] = []
    run: list[Reading] = []
    for reading in sorted(readings, key=lambda r: r.recorded_at):
        if _deviation(reading.temperature_c, low, high) > 0:
            run.append(reading)
            continue
        if run:
            runs.append(run)
            run = []
    if run:
        runs.append(run)

    excursions: list[Excursion] = []
    for run in runs:
        worst = max(run, key=lambda r: _deviation(r.temperature_c, low, high))
        duration = run[-1].recorded_at - run[0].recorded_at
        if duration < grace and _deviation(worst.temperature_c, low, high) < HARD_DEVIATION_C:
            continue  # short door-open spike, tolerated per SOP-TR-07
        excursions.append(Excursion(run[0].recorded_at, run[-1].recorded_at, worst.temperature_c))
    return excursions
