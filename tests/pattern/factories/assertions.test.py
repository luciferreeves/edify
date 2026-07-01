"""Tests for the functional lookaround assertion factories."""

from edify import (
    DIGIT,
    Pattern,
    assert_ahead,
    assert_behind,
    assert_not_ahead,
    assert_not_behind,
)


def test_assert_ahead_emits_positive_lookahead():
    assert assert_ahead(DIGIT).to_regex_string() == "(?=\\d)"


def test_assert_not_ahead_emits_negative_lookahead():
    assert assert_not_ahead(DIGIT).to_regex_string() == "(?!\\d)"


def test_assert_behind_emits_positive_lookbehind():
    assert assert_behind(DIGIT).to_regex_string() == "(?<=\\d)"


def test_assert_not_behind_emits_negative_lookbehind():
    assert assert_not_behind(DIGIT).to_regex_string() == "(?<!\\d)"


def test_assert_ahead_returns_a_pattern_instance():
    assert isinstance(assert_ahead(DIGIT), Pattern)
