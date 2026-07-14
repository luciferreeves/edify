from edify import Pattern
from edify.atoms import signed


def _anchored():
    return Pattern().start_of_input().use(signed).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("+42")


def test_rejects_off_shape_input():
    assert not _anchored()("42")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(signed).end_of_input()
    assert embedded("v=" + "+42")
    assert not embedded("+42")


def test_atom_regex_string_is_non_empty():
    fragment = signed.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
