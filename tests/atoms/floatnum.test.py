from edify import Pattern
from edify.atoms import floatnum


def _anchored():
    return Pattern().start_of_input().use(floatnum).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("1.5e10")


def test_rejects_off_shape_input():
    assert not _anchored()("abc")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(floatnum).end_of_input()
    assert embedded("v=" + "1.5e10")
    assert not embedded("1.5e10")


def test_atom_regex_string_is_non_empty():
    fragment = floatnum.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
