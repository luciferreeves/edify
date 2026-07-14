from edify import Pattern
from edify.atoms import oid


def _anchored():
    return Pattern().start_of_input().use(oid).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("1.3.6.1.4.1")


def test_rejects_off_shape_input():
    assert not _anchored()("1")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(oid).end_of_input()
    assert embedded("v=" + "1.3.6.1.4.1")
    assert not embedded("1.3.6.1.4.1")


def test_atom_regex_string_is_non_empty():
    fragment = oid.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
