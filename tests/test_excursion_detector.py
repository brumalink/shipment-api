from datetime import datetime, timedelta

import pytest

from app.services.excursion_detector import Reading, detect

T0 = datetime(2025, 5, 1, 8, 0)


def series(*temps: float) -> list[Reading]:
    """One reading every 5 minutes, like a BL-T3 tracker in normal mode."""
    return [Reading(T0 + timedelta(minutes=5 * i), t) for i, t in enumerate(temps)]


def test_all_in_range_has_no_excursions():
    assert detect(series(4.0, 5.1, 6.3, 7.9)) == []


def test_sustained_excursion_is_reported_with_peak():
    result = detect(series(5.0, 8.4, 9.6, 8.9, 8.5, 6.0))  # 15 minutes above 8 C
    assert len(result) == 1
    assert result[0].peak_c == 9.6
    assert result[0].started_at == T0 + timedelta(minutes=5)


def test_short_door_open_spike_is_tolerated():
    assert detect(series(5.0, 9.0, 8.7, 6.0)) == []  # 5 minutes, +1 C


def test_short_but_severe_spike_is_reported():
    assert len(detect(series(5.0, 14.0, 13.5, 6.0))) == 1  # 5 minutes, but +6 C


def test_too_cold_is_an_excursion_too():
    assert len(detect(series(3.0, 1.2, 0.8, 1.0, 3.5))) == 1


def test_room_temperature_profile():
    assert detect(series(18.0, 22.0, 24.9), profile="15-25C") == []
    assert len(detect(series(20.0, 26.5, 27.0, 26.1, 20.0), profile="15-25C")) == 1


def test_frozen_profile():
    assert len(detect(series(-20.0, -12.0, -11.0, -11.5, -20.0), profile="frozen")) == 1


def test_unknown_profile_is_rejected():
    with pytest.raises(ValueError):
        detect(series(5.0), profile="ambient")
