from edify import Pattern
from edify.atoms import label


def _anchored():
    return Pattern().start_of_input().use(label).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("example")


def test_rejects_off_shape_input():
    assert not _anchored()("-bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(label).end_of_input()
    assert embedded("v=" + "example")
    assert not embedded("example")


def test_atom_regex_string_is_non_empty():
    fragment = label.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
