from edify import Pattern
from edify.atoms import httpstatus


def _anchored():
    return Pattern().start_of_input().use(httpstatus).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("200")


def test_rejects_off_shape_input():
    assert not _anchored()("600")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(httpstatus).end_of_input()
    assert embedded("v=" + "200")
    assert not embedded("200")


def test_atom_regex_string_is_non_empty():
    fragment = httpstatus.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
