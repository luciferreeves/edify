from edify import Pattern
from edify.atoms import clock12


def _anchored():
    return Pattern().start_of_input().use(clock12).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("12:00 PM")


def test_rejects_off_shape_input():
    assert not _anchored()("13:00 PM")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(clock12).end_of_input()
    assert embedded("v=" + "12:00 PM")
    assert not embedded("12:00 PM")


def test_atom_regex_string_is_non_empty():
    fragment = clock12.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
