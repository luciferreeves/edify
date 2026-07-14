from edify import Pattern
from edify.atoms import cidr


def _anchored():
    return Pattern().start_of_input().use(cidr).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("10.0.0.0/8")


def test_rejects_off_shape_input():
    assert not _anchored()("10.0.0.0")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(cidr).end_of_input()
    assert embedded("v=" + "10.0.0.0/8")
    assert not embedded("10.0.0.0/8")


def test_atom_regex_string_is_non_empty():
    fragment = cidr.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
