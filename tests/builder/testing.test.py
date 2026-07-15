"""Tests for the ``assert_matches`` / ``assert_rejects`` helpers."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.testing import PatternDidNotMatchInputsError, PatternMatchedRejectedInputsError


def _digits_pattern():
    return Pattern().one_or_more().digit()


def test_assert_matches_returns_self_when_every_input_matches():
    pattern = _digits_pattern()
    result = pattern.assert_matches(["12", "3", "999"])
    assert result is pattern


def test_assert_matches_raises_when_at_least_one_input_does_not_match():
    with pytest.raises(PatternDidNotMatchInputsError) as excinfo:
        _digits_pattern().assert_matches(["12", "abc", "999"])
    text = str(excinfo.value)
    assert "'abc'" in text
    assert "did not match" in text
    assert "= note:" in text


def test_assert_matches_reports_every_missing_input_at_once():
    with pytest.raises(PatternDidNotMatchInputsError) as excinfo:
        _digits_pattern().assert_matches(["abc", "xyz", "42"])
    assert excinfo.value.missing_matches == ("abc", "xyz")


def test_assert_rejects_returns_self_when_every_input_is_rejected():
    pattern = _digits_pattern()
    result = pattern.assert_rejects(["abc", "xyz"])
    assert result is pattern


def test_assert_rejects_raises_when_at_least_one_input_matches():
    with pytest.raises(PatternMatchedRejectedInputsError) as excinfo:
        _digits_pattern().assert_rejects(["abc", "42"])
    text = str(excinfo.value)
    assert "'42'" in text
    assert "expected to be rejected" in text


def test_assert_rejects_reports_every_unexpected_match_at_once():
    with pytest.raises(PatternMatchedRejectedInputsError) as excinfo:
        _digits_pattern().assert_rejects(["abc", "42", "999"])
    assert excinfo.value.unexpected_matches == ("42", "999")


def test_assert_matches_works_on_regex_builder_too():
    builder = RegexBuilder().one_or_more().digit()
    assert builder.assert_matches(["1", "22", "333"]) is builder


def test_assert_rejects_works_on_regex_builder_too():
    builder = RegexBuilder().one_or_more().digit()
    assert builder.assert_rejects(["abc", ""]) is builder


def test_assert_matches_accepts_any_iterable_not_only_lists():
    pattern = _digits_pattern()
    assert pattern.assert_matches(iter(["1", "22", "333"])) is pattern


def test_assert_rejects_accepts_any_iterable_not_only_lists():
    pattern = _digits_pattern()
    assert pattern.assert_rejects(iter(["abc", ""])) is pattern
