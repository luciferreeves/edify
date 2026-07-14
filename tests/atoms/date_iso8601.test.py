from edify import Pattern
from edify.atoms import date_iso8601


def _anchored():
    return Pattern().start_of_input().use(date_iso8601).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("2024-01-15")


def test_rejects_off_shape_input():
    assert not _anchored()("2024/01/15")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(date_iso8601).end_of_input()
    assert embedded("v=" + "2024-01-15")
    assert not embedded("2024-01-15")


def test_atom_regex_string_is_non_empty():
    fragment = date_iso8601.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
