from edify import Pattern
from edify.atoms import month


def _anchored():
    return Pattern().start_of_input().use(month).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("07")


def test_rejects_off_shape_input():
    assert not _anchored()("13")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(month).end_of_input()
    assert embedded("v=" + "07")
    assert not embedded("07")


def test_atom_regex_string_is_non_empty():
    fragment = month.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
