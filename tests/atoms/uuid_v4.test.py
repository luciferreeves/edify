from edify import Pattern
from edify.atoms import uuid_v4


def _anchored():
    return Pattern().start_of_input().use(uuid_v4).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("550e8400-e29b-41d4-a716-446655440000")


def test_rejects_off_shape_input():
    assert not _anchored()("nope")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(uuid_v4).end_of_input()
    assert embedded("v=" + "550e8400-e29b-41d4-a716-446655440000")
    assert not embedded("550e8400-e29b-41d4-a716-446655440000")


def test_atom_regex_string_is_non_empty():
    fragment = uuid_v4.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
