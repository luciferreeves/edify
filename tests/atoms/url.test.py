from edify import Pattern
from edify.atoms import url


def _anchored():
    return Pattern().start_of_input().use(url).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("https://example.com")


def test_rejects_off_shape_input():
    assert not _anchored()("not a url")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(url).end_of_input()
    assert embedded("v=" + "https://example.com")
    assert not embedded("https://example.com")


def test_atom_regex_string_is_non_empty():
    fragment = url.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
