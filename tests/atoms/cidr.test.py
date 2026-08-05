import pytest

from edify import Pattern, library
from edify.atoms import cidr

ACCEPTED = [
    "10.0.0.0/8",
    "10.0.0.0/0",
    "10.0.0.0/24",
    "10.0.0.0/29",
    "10.0.0.0/30",
    "10.0.0.0/32",
    "0.0.0.0/0",
    "255.255.255.255/32",
]

REJECTED = [
    "10.0.0.0",
    "10.0.0.0/",
    "10.0.0.0/33",
    "10.0.0.0/40",
    "10.0.0.0/99",
    "10.0.0.0/100",
    "10.0.0.0/08",
    "10.0.0.0/-1",
    "256.0.0.0/24",
]


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


@pytest.mark.parametrize("block", ACCEPTED)
def test_accepts_valid_blocks(block: str):
    assert _anchored()(block)


@pytest.mark.parametrize("block", REJECTED)
def test_rejects_invalid_blocks(block: str):
    assert not _anchored()(block)


@pytest.mark.parametrize("length", range(33))
def test_accepts_every_valid_prefix_length(length: int):
    assert _anchored()(f"10.0.0.0/{length}")


@pytest.mark.parametrize("length", range(33, 100))
def test_rejects_every_prefix_length_above_thirty_two(length: int):
    assert not _anchored()(f"10.0.0.0/{length}")


@pytest.mark.parametrize("block", ACCEPTED)
def test_never_accepts_what_the_validator_rejects(block: str):
    assert library.cidr(block)
