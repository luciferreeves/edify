"""Tests for the ``+`` and ``|`` operators on :class:`RegexBuilder`."""

from edify import DIGIT, END, START, Pattern, RegexBuilder


def test_plus_concatenates_a_builder_with_a_pattern():
    combined = RegexBuilder().string("hello") + Pattern().string("world")
    assert combined.to_regex_string() == "helloworld"


def test_plus_returns_a_regex_builder_instance():
    combined = RegexBuilder().digit() + Pattern().word()
    assert isinstance(combined, RegexBuilder)


def test_plus_preserves_anchors_from_the_right_hand_operand():
    combined = RegexBuilder() + START + DIGIT + END
    assert combined.to_regex_string() == "^\\d$"


def test_or_produces_alternation_starting_from_a_builder():
    combined = RegexBuilder().string("cat") | Pattern().string("dog")
    assert combined.to_regex_string() == "(?:cat|dog)"


def test_or_returns_a_regex_builder_instance():
    combined = RegexBuilder().digit() | Pattern().word()
    assert isinstance(combined, RegexBuilder)


def test_plus_leaves_the_original_builder_untouched():
    original = RegexBuilder().string("abc")
    _ = original + Pattern().string("def")
    assert original.to_regex_string() == "abc"
