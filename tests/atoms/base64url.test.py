from edify import Pattern
from edify.atoms import base64url


def _anchored():
    return Pattern().start_of_input().use(base64url).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("Hello_World-")


def test_rejects_off_shape_input():
    assert not _anchored()("!")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(base64url).end_of_input()
    assert embedded("v=" + "Hello_World-")
    assert not embedded("Hello_World-")


def test_atom_regex_string_is_non_empty():
    fragment = base64url.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
