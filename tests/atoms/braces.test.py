from edify import Pattern
from edify.atoms import braces


def _anchored():
    return Pattern().start_of_input().use(braces).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("{hello}")


def test_rejects_off_shape_input():
    assert not _anchored()("hello")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(braces).end_of_input()
    assert embedded("v=" + "{hello}")
    assert not embedded("{hello}")


def test_atom_regex_string_is_non_empty():
    fragment = braces.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
