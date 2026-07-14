from edify import Pattern
from edify.atoms import extension


def _anchored():
    return Pattern().start_of_input().use(extension).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()(".txt")


def test_rejects_off_shape_input():
    assert not _anchored()("txt")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(extension).end_of_input()
    assert embedded("v=" + ".txt")
    assert not embedded(".txt")


def test_atom_regex_string_is_non_empty():
    fragment = extension.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
