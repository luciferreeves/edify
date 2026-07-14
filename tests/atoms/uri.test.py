from edify import Pattern
from edify.atoms import uri


def _anchored():
    return Pattern().start_of_input().use(uri).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("mailto:x@y.com")


def test_rejects_off_shape_input():
    assert not _anchored()("just")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(uri).end_of_input()
    assert embedded("v=" + "mailto:x@y.com")
    assert not embedded("mailto:x@y.com")


def test_atom_regex_string_is_non_empty():
    fragment = uri.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
