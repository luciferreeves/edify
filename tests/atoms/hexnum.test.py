from edify import Pattern
from edify.atoms import hexnum


def _anchored():
    return Pattern().start_of_input().use(hexnum).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("0xFF")


def test_rejects_off_shape_input():
    assert not _anchored()("FF")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(hexnum).end_of_input()
    assert embedded("v=" + "0xFF")
    assert not embedded("0xFF")


def test_atom_regex_string_is_non_empty():
    fragment = hexnum.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
