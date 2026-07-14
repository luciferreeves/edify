from edify import Pattern
from edify.atoms import sha256


def _anchored():
    return Pattern().start_of_input().use(sha256).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def test_rejects_off_shape_input():
    assert not _anchored()("short")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(sha256).end_of_input()
    assert embedded("v=" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    assert not embedded("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def test_atom_regex_string_is_non_empty():
    fragment = sha256.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
