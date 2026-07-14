from edify import Pattern
from edify.atoms import filename


def _anchored():
    return Pattern().start_of_input().use(filename).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("myfile.txt")


def test_rejects_off_shape_input():
    assert not _anchored()("bad/path")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(filename).end_of_input()
    assert embedded("v=" + "myfile.txt")
    assert not embedded("myfile.txt")


def test_atom_regex_string_is_non_empty():
    fragment = filename.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
