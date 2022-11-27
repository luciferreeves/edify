from edify.library import zip


def test_valid_zips():
    zips = {"12345": True, "12345-1234": True, "12345-123456": False, "1234": False}
    for zip_string, expectation in zips.items():
        assert zip(zip_string) == expectation


def test_invalid_locale():
    try:
        zip("12345", locale="INVALID")
    except ValueError:
        assert True


def test_invalid_locale_type():
    try:
        zip("12345", 5)
    except TypeError:
        assert True


def test_empty_locale():
    try:
        zip("12345", "")
    except ValueError:
        assert True


def test_locale_IN():
    zips = {"123456": True, "000000": False, "012345": False, "12345": False, "1234567": False}
    for zip_string, expectation in zips.items():
        assert zip(zip_string, locale="IN") == expectation
