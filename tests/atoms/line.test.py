from edify import Pattern
from edify.atoms import line


def _anchored():
    return Pattern().start_of_input().use(line).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("hello world")


def test_rejects_off_shape_input():
    assert not _anchored()("\n")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(line).end_of_input()
    assert embedded("v=" + "hello world")
    assert not embedded("hello world")


def test_atom_regex_string_is_non_empty():
    fragment = line.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
