"""Tests for the ``+`` and ``|`` operators on :class:`Pattern`."""

from edify import DIGIT, END, START, WORD, Pattern


def test_plus_concatenates_two_patterns():
    combined = Pattern().string("hello") + Pattern().string("world")
    assert combined.to_regex_string() == "helloworld"


def test_plus_preserves_anchors_from_both_operands():
    combined = START + Pattern().exactly(4).digit() + END
    assert combined.to_regex_string() == "^\\d{4}$"


def test_plus_returns_a_new_pattern_and_leaves_operands_untouched():
    left = Pattern().digit()
    right = Pattern().word()
    combined = left + right
    assert combined is not left
    assert combined is not right
    assert left.to_regex_string() == "\\d"
    assert right.to_regex_string() == "\\w"


def test_plus_using_module_constants_produces_expected_string():
    combined = DIGIT + WORD
    assert combined.to_regex_string() == "\\d\\w"


def test_or_produces_alternation_between_two_patterns():
    combined = Pattern().string("http") | Pattern().string("https")
    assert combined.to_regex_string() == "(?:http|https)"


def test_or_returns_a_new_pattern_and_leaves_operands_untouched():
    left = Pattern().string("cat")
    right = Pattern().string("dog")
    combined = left | right
    assert combined is not left
    assert combined is not right
    assert left.to_regex_string() == "cat"
    assert right.to_regex_string() == "dog"


def test_or_chaining_produces_three_way_alternation():
    combined = Pattern().string("cat") | Pattern().string("dog") | Pattern().string("fish")
    assert combined.to_regex_string() == "(?:(?:cat|dog)|fish)"


def test_plus_composes_with_or_to_form_a_realistic_pattern():
    scheme = Pattern().string("http") | Pattern().string("https")
    combined = scheme + Pattern().string("://")
    assert combined.to_regex_string() == "(?:http|https)://"
