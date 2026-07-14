from edify import Pattern
from edify.atoms import bic


def _anchored():
    return Pattern().start_of_input().use(bic).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("DEUTDEFF500")


def test_rejects_off_shape_input():
    assert not _anchored()("bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(bic).end_of_input()
    assert embedded("v=" + "DEUTDEFF500")
    assert not embedded("DEUTDEFF500")


def test_atom_regex_string_is_non_empty():
    fragment = bic.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
