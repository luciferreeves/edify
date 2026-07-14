from edify import Pattern
from edify.atoms import isodatetime


def _anchored():
    return Pattern().start_of_input().use(isodatetime).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("2024-01-15T12:00:00Z")


def test_rejects_off_shape_input():
    assert not _anchored()("bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(isodatetime).end_of_input()
    assert embedded("v=" + "2024-01-15T12:00:00Z")
    assert not embedded("2024-01-15T12:00:00Z")


def test_atom_regex_string_is_non_empty():
    fragment = isodatetime.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
