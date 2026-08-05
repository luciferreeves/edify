import pytest

from edify import Pattern, library
from edify.atoms import ipv6

ACCEPTED = [
    "2001:db8:0:0:0:0:0:1",
    "1:2:3:4:5:6:7:8",
    "2001:db8::",
    "1:2:3:4:5:6:7::",
    "::",
    "::1",
    "::ffff:0:0",
    "2001:db8::1",
    "1::8",
    "1:2:3:4:5:6::8",
    "2001:db8:1::2:3",
    "fe80::1:2:3:4",
    "1::2:3:4:5:6:7",
    "ABCD:ef01::1",
]

REJECTED = [
    "not_ipv6",
    "",
    "1:2:3:4:5:6:7",
    "1:2:3:4:5:6:7:8:9",
    "1::2::3",
    "2001:db8:::1",
    "12345::",
    "g::1",
    ":1",
    "1:",
]


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


@pytest.mark.parametrize("address", ACCEPTED)
def test_accepts_every_documented_form(address: str):
    assert _anchored()(address)


@pytest.mark.parametrize("address", REJECTED)
def test_rejects_malformed_addresses(address: str):
    assert not _anchored()(address)


@pytest.mark.parametrize("position", range(1, 7))
def test_accepts_compression_at_every_interior_position(position: int):
    groups = ["1", "2", "3", "4", "5", "6"]
    address = ":".join(groups[:position]) + "::" + ":".join(groups[position:])
    assert _anchored()(address)


@pytest.mark.parametrize("address", ACCEPTED)
def test_never_accepts_what_the_validator_rejects(address: str):
    assert library.ipv6(address)
