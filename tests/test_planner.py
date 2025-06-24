import pytest

from app.routing.planner import distance_km, plan_route


def test_distance_warsaw_wroclaw_is_plausible():
    assert 290 < distance_km("WAW", "WRO") < 310


def test_short_trip_is_direct():
    assert plan_route("WAW", "WRO") == ["WAW", "WRO"]


def test_long_trip_goes_through_a_hub():
    # Warsaw-Berlin is ~520 km, over the single-leg limit, so it goes via Poznan.
    assert plan_route("WAW", "BER") == ["WAW", "POZ", "BER"]


def test_same_hub():
    assert plan_route("KRK", "KRK") == ["KRK"]


def test_unknown_hub():
    with pytest.raises(ValueError):
        plan_route("WAW", "LON")
