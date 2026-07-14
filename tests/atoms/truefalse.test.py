from edify import Pattern
from edify.atoms import truefalse


def _anchored():
    return Pattern().start_of_input().use(truefalse).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("true")


def test_rejects_off_shape_input():
    assert not _anchored()("maybe")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(truefalse).end_of_input()
    assert embedded("v=" + "true")
    assert not embedded("true")


def test_atom_regex_string_is_non_empty():
    fragment = truefalse.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
