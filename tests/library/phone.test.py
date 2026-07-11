from edify.library import phone


def test_valid_phone():
    assert phone("+1-555-1234")


def test_short_phone():
    assert phone("911")


def test_bad_phone():
    assert not phone("!!!")
