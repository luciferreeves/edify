"""Tests for alternation rendering branches not covered by the main builder tests."""

from edify import RegexBuilder


def test_any_of_with_only_non_fusable_members():
    expr = RegexBuilder().any_of().string("hello").digit().end()
    assert expr.to_regex_string() == "(?:hello|\\d)"


def test_any_of_with_any_of_chars_member():
    expr = RegexBuilder().any_of().any_of_chars("xyz").end()
    assert expr.to_regex_string() == "[xyz]"
