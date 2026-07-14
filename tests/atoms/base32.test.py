from edify import Pattern
from edify.atoms import base32


def _anchored():
    return Pattern().start_of_input().use(base32).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("JBSWY3DP===")


def test_rejects_off_shape_input():
    assert not _anchored()("lower")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(base32).end_of_input()
    assert embedded("v=" + "JBSWY3DP===")
    assert not embedded("JBSWY3DP===")


def test_atom_regex_string_is_non_empty():
    fragment = base32.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
