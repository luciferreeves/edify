from edify import Pattern
from edify.atoms import base58


def _anchored():
    return Pattern().start_of_input().use(base58).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("3P3Ceff5tj")


def test_rejects_off_shape_input():
    assert not _anchored()("0")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(base58).end_of_input()
    assert embedded("v=" + "3P3Ceff5tj")
    assert not embedded("3P3Ceff5tj")


def test_atom_regex_string_is_non_empty():
    fragment = base58.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
