from edify import Pattern
from edify.atoms import money


def _anchored():
    return Pattern().start_of_input().use(money).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("USD 100.50")


def test_rejects_off_shape_input():
    assert not _anchored()("bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(money).end_of_input()
    assert embedded("v=" + "USD 100.50")
    assert not embedded("USD 100.50")


def test_atom_regex_string_is_non_empty():
    fragment = money.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
