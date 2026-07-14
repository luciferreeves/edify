from edify import Pattern
from edify.atoms import ipv6


def _anchored():
    return Pattern().start_of_input().use(ipv6).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("2001:db8:0:0:0:0:0:1")


def test_rejects_off_shape_input():
    assert not _anchored()("not_ipv6")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(ipv6).end_of_input()
    assert embedded("v=" + "2001:db8:0:0:0:0:0:1")
    assert not embedded("2001:db8:0:0:0:0:0:1")


def test_atom_regex_string_is_non_empty():
    fragment = ipv6.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
