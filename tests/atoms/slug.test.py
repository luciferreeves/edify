from edify import Pattern
from edify.atoms import slug


def _anchored():
    return Pattern().start_of_input().use(slug).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("my-slug")


def test_rejects_off_shape_input():
    assert not _anchored()("-bad")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(slug).end_of_input()
    assert embedded("v=" + "my-slug")
    assert not embedded("my-slug")


def test_atom_regex_string_is_non_empty():
    fragment = slug.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
