from datetime import datetime, timedelta

from app.services.excursion_detector import Reading, detect

T0 = datetime(2025, 4, 1, 8, 0)


def series(*temps: float) -> list[Reading]:
    return [Reading(T0 + timedelta(minutes=5 * i), t) for i, t in enumerate(temps)]


def test_all_in_range_has_no_excursions():
    assert detect(series(4.0, 5.1, 6.3, 7.9)) == []


def test_single_excursion_is_reported_with_peak():
    result = detect(series(5.0, 8.4, 9.6, 8.9, 6.0))
    assert len(result) == 1
    assert result[0].peak_c == 9.6
    assert result[0].started_at == T0 + timedelta(minutes=5)


def test_too_cold_is_an_excursion_too():
    assert len(detect(series(3.0, 1.2, 0.8, 3.5))) == 1
