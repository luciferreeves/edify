import pytest

from edify.library import zip

_DEFAULT_US_ZIPS = {
    "12345": True,
    "12345-1234": True,
    "12345-123456": False,
    "1234": False,
}

_INDIA_ZIPS = {
    "123456": True,
    "000000": False,
    "012345": False,
    "12345": False,
    "1234567": False,
}


def test_valid_zips():
    for candidate, expectation in _DEFAULT_US_ZIPS.items():
        assert zip(candidate) is expectation


def test_invalid_locale():
    with pytest.raises(ValueError, match="locale must be one of"):
        zip("12345", locale="INVALID")


def test_invalid_locale_type():
    with pytest.raises(TypeError, match="locale must be a string"):
        zip("12345", 5)


def test_empty_locale():
    with pytest.raises(ValueError, match="locale cannot be empty"):
        zip("12345", "")


def test_locale_india():
    for candidate, expectation in _INDIA_ZIPS.items():
        assert zip(candidate, locale="IN") is expectation
