from edify import Pattern
from edify.atoms import email


def _anchored():
    return Pattern().start_of_input().use(email).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("user@example.com")


def test_rejects_off_shape_input():
    assert not _anchored()("not email")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(email).end_of_input()
    assert embedded("v=" + "user@example.com")
    assert not embedded("user@example.com")


def test_atom_regex_string_is_non_empty():
    fragment = email.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
