from edify import Pattern
from edify.atoms import decimal


def _anchored():
    return Pattern().start_of_input().use(decimal).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("3.14")


def test_rejects_off_shape_input():
    assert not _anchored()("3")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(decimal).end_of_input()
    assert embedded("v=" + "3.14")
    assert not embedded("3.14")


def test_atom_regex_string_is_non_empty():
    fragment = decimal.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
