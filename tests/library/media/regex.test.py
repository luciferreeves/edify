from edify.library import regex


def test_valid_regex():
    assert regex(r"^\d+$")


def test_invalid_regex():
    assert not regex(r"(?P<name>")


def test_non_string():
    assert not regex(42)
