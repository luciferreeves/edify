from edify import Pattern
from edify.atoms import printable


def _anchored():
    return Pattern().start_of_input().use(printable).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("!")


def test_rejects_off_shape_input():
    assert not _anchored()("\x00")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(printable).end_of_input()
    assert embedded("v=" + "!")
    assert not embedded("!")


def test_atom_regex_string_is_non_empty():
    fragment = printable.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
