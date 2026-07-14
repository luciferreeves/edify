from edify import Pattern
from edify.atoms import ulid


def _anchored():
    return Pattern().start_of_input().use(ulid).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("01ARZ3NDEKTSV4RRFFQ69G5FAV")


def test_rejects_off_shape_input():
    assert not _anchored()("short")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(ulid).end_of_input()
    assert embedded("v=" + "01ARZ3NDEKTSV4RRFFQ69G5FAV")
    assert not embedded("01ARZ3NDEKTSV4RRFFQ69G5FAV")


def test_atom_regex_string_is_non_empty():
    fragment = ulid.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
