from edify import Pattern
from edify.atoms import year


def _anchored():
    return Pattern().start_of_input().use(year).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("2024")


def test_rejects_off_shape_input():
    assert not _anchored()("24")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(year).end_of_input()
    assert embedded("v=" + "2024")
    assert not embedded("2024")


def test_atom_regex_string_is_non_empty():
    fragment = year.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
