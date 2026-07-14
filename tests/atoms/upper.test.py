from edify import Pattern
from edify.atoms import upper


def _anchored():
    return Pattern().start_of_input().use(upper).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("A")


def test_rejects_off_shape_input():
    assert not _anchored()("a")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(upper).end_of_input()
    assert embedded("v=" + "A")
    assert not embedded("A")


def test_atom_regex_string_is_non_empty():
    fragment = upper.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
