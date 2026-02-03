import pytest

from app.models.tenant import validate_slug


@pytest.mark.parametrize("slug", ["pharmalog", "nordic-3pl", "coldway-cz"])
def test_valid_slugs(slug):
    assert validate_slug(slug) == slug


@pytest.mark.parametrize("slug", ["", "ab", "3pl-first", "Upper", "trailing-", "double--dash", "a" * 40])
def test_invalid_slugs(slug):
    with pytest.raises(ValueError):
        validate_slug(slug)
