from edify import Pattern
from edify.atoms import port_number


def _anchored():
    return Pattern().start_of_input().use(port_number).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("65535")


def test_rejects_off_shape_input():
    assert not _anchored()("65536")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(port_number).end_of_input()
    assert embedded("v=" + "65535")
    assert not embedded("65535")


def test_atom_regex_string_is_non_empty():
    fragment = port_number.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
