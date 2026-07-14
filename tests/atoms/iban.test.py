from edify import Pattern
from edify.atoms import iban


def _anchored():
    return Pattern().start_of_input().use(iban).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("GB33BUKB20201555555555")


def test_rejects_off_shape_input():
    assert not _anchored()("bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(iban).end_of_input()
    assert embedded("v=" + "GB33BUKB20201555555555")
    assert not embedded("GB33BUKB20201555555555")


def test_atom_regex_string_is_non_empty():
    fragment = iban.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
