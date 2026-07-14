from edify import Pattern
from edify.atoms import mac


def _anchored():
    return Pattern().start_of_input().use(mac).end_of_input()


def test_accepts_sample_from_shape():
    assert _anchored()("aa:bb:cc:dd:ee:ff")


def test_rejects_off_shape_input():
    assert not _anchored()("not-a-mac")


def test_atom_composes_inside_a_larger_pattern():
    embedded = Pattern().start_of_input().string("v=").use(mac).end_of_input()
    assert embedded("v=" + "aa:bb:cc:dd:ee:ff")
    assert not embedded("aa:bb:cc:dd:ee:ff")


def test_atom_regex_string_is_non_empty():
    fragment = mac.to_regex_string()
    assert fragment
    assert isinstance(fragment, str)
