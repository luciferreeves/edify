from edify import Pattern
from edify.atoms import objectid


def _anchored():
    return Pattern().start_of_input().use(objectid).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("507f1f77bcf86cd799439011")


def test_rejects_off_shape_input():
    assert not _anchored()("short")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(objectid).end_of_input()
    assert embedded("v=" + "507f1f77bcf86cd799439011")
    assert not embedded("507f1f77bcf86cd799439011")


def test_atom_regex_string_is_non_empty():
    fragment = objectid.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
