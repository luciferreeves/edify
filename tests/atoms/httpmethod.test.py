from edify import Pattern
from edify.atoms import httpmethod


def _anchored():
    return Pattern().start_of_input().use(httpmethod).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("POST")


def test_rejects_off_shape_input():
    assert not _anchored()("FOO")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(httpmethod).end_of_input()
    assert embedded("v=" + "POST")
    assert not embedded("POST")


def test_atom_regex_string_is_non_empty():
    fragment = httpmethod.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
