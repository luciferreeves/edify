"""Tests for the ``.use(pattern)`` chain method on :class:`RegexBuilder`."""

from edify import Pattern, RegexBuilder


def test_use_embeds_a_pattern_at_the_current_position():
    username = Pattern().between(3, 20).word()
    expression = RegexBuilder().string("User ").use(username)
    assert expression.to_regex_string() == "User \\w{3,20}"


def test_use_composes_multiple_patterns_in_sequence():
    first_pattern = Pattern().exactly(3).digit()
    second_pattern = Pattern().char("-")
    third_pattern = Pattern().exactly(4).digit()
    expression = RegexBuilder().use(first_pattern).use(second_pattern).use(third_pattern)
    assert expression.to_regex_string() == "\\d{3}\\-\\d{4}"


def test_use_drops_the_pattern_flag_snapshot_by_default():
    case_insensitive_pattern = Pattern().ignore_case().string("hello")
    expression = RegexBuilder().use(case_insensitive_pattern)
    compiled = expression.to_regex()
    assert compiled.flags & 2 == 0


def test_use_accepts_another_regex_builder_as_the_source():
    fragment = RegexBuilder().one_or_more().digit()
    expression = RegexBuilder().string("id=").use(fragment)
    assert expression.to_regex_string() == "id=\\d+"
