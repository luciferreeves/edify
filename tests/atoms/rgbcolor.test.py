from edify import Pattern
from edify.atoms import rgbcolor


def _anchored():
    return Pattern().start_of_input().use(rgbcolor).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("rgb(255, 0, 0)")


def test_rejects_off_shape_input():
    assert not _anchored()("nope")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(rgbcolor).end_of_input()
    assert embedded("v=" + "rgb(255, 0, 0)")
    assert not embedded("rgb(255, 0, 0)")


def test_atom_regex_string_is_non_empty():
    fragment = rgbcolor.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
