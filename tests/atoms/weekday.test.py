from edify import Pattern
from edify.atoms import weekday


def _anchored():
    return Pattern().start_of_input().use(weekday).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("Mon")


def test_rejects_off_shape_input():
    assert not _anchored()("Xyz")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(weekday).end_of_input()
    assert embedded("v=" + "Mon")
    assert not embedded("Mon")


def test_atom_regex_string_is_non_empty():
    fragment = weekday.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
