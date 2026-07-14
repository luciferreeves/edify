from edify import Pattern
from edify.atoms import hex_color


def _anchored():
    return Pattern().start_of_input().use(hex_color).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("#abc")


def test_rejects_off_shape_input():
    assert not _anchored()("nope")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(hex_color).end_of_input()
    assert embedded("v=" + "#abc")
    assert not embedded("#abc")


def test_atom_regex_string_is_non_empty():
    fragment = hex_color.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
