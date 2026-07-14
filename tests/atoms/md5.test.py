from edify import Pattern
from edify.atoms import md5


def _anchored():
    return Pattern().start_of_input().use(md5).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def test_rejects_off_shape_input():
    assert not _anchored()("short")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(md5).end_of_input()
    assert embedded("v=" + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    assert not embedded("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


def test_atom_regex_string_is_non_empty():
    fragment = md5.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
