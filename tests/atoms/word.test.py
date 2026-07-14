from edify import Pattern
from edify.atoms import word


def _anchored():
    return Pattern().start_of_input().use(word).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("hello_1")


def test_rejects_off_shape_input():
    assert not _anchored()("has space")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(word).end_of_input()
    assert embedded("v=" + "hello_1")
    assert not embedded("hello_1")


def test_atom_regex_string_is_non_empty():
    fragment = word.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
