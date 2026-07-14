from edify import Pattern
from edify.atoms import time_24h


def _anchored():
    return Pattern().start_of_input().use(time_24h).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("23:59")


def test_rejects_off_shape_input():
    assert not _anchored()("24:00")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(time_24h).end_of_input()
    assert embedded("v=" + "23:59")
    assert not embedded("23:59")


def test_atom_regex_string_is_non_empty():
    fragment = time_24h.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
