from edify import Pattern
from edify.atoms import hostname


def _anchored():
    return Pattern().start_of_input().use(hostname).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("a.b.c")


def test_rejects_off_shape_input():
    assert not _anchored()("-nope")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(hostname).end_of_input()
    assert embedded("v=" + "a.b.c")
    assert not embedded("a.b.c")


def test_atom_regex_string_is_non_empty():
    fragment = hostname.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
