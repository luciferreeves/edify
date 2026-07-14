from edify import Pattern
from edify.atoms import lower


def _anchored():
    return Pattern().start_of_input().use(lower).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("a")


def test_rejects_off_shape_input():
    assert not _anchored()("A")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(lower).end_of_input()
    assert embedded("v=" + "a")
    assert not embedded("a")


def test_atom_regex_string_is_non_empty():
    fragment = lower.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
