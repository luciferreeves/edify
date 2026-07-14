from edify import Pattern
from edify.atoms import currency


def _anchored():
    return Pattern().start_of_input().use(currency).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("USD")


def test_rejects_off_shape_input():
    assert not _anchored()("us")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(currency).end_of_input()
    assert embedded("v=" + "USD")
    assert not embedded("USD")


def test_atom_regex_string_is_non_empty():
    fragment = currency.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
