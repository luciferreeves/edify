from edify import Pattern
from edify.atoms import base64


def _anchored():
    return Pattern().start_of_input().use(base64).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("SGVsbG8=")


def test_rejects_off_shape_input():
    assert not _anchored()("!!")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(base64).end_of_input()
    assert embedded("v=" + "SGVsbG8=")
    assert not embedded("SGVsbG8=")


def test_atom_regex_string_is_non_empty():
    fragment = base64.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
