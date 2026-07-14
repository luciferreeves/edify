from edify import Pattern
from edify.atoms import filepath


def _anchored():
    return Pattern().start_of_input().use(filepath).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("/home/user")


def test_rejects_off_shape_input():
    assert not _anchored()("")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(filepath).end_of_input()
    assert embedded("v=" + "/home/user")
    assert not embedded("/home/user")


def test_atom_regex_string_is_non_empty():
    fragment = filepath.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
