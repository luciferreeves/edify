from edify import Pattern
from edify.atoms import duration


def _anchored():
    return Pattern().start_of_input().use(duration).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("P1Y")


def test_rejects_off_shape_input():
    assert not _anchored()("P")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(duration).end_of_input()
    assert embedded("v=" + "P1Y")
    assert not embedded("P1Y")


def test_atom_regex_string_is_non_empty():
    fragment = duration.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
