from edify import Pattern
from edify.atoms import ipv4_octet


def _anchored():
    return Pattern().start_of_input().use(ipv4_octet).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("192")


def test_rejects_off_shape_input():
    assert not _anchored()("999")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(ipv4_octet).end_of_input()
    assert embedded("v=" + "192")
    assert not embedded("192")


def test_atom_regex_string_is_non_empty():
    fragment = ipv4_octet.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
