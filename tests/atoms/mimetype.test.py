from edify import Pattern
from edify.atoms import mimetype


def _anchored():
    return Pattern().start_of_input().use(mimetype).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("text/plain")


def test_rejects_off_shape_input():
    assert not _anchored()("text")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(mimetype).end_of_input()
    assert embedded("v=" + "text/plain")
    assert not embedded("text/plain")


def test_atom_regex_string_is_non_empty():
    fragment = mimetype.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
