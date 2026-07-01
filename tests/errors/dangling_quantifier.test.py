"""Tests for :class:`DanglingQuantifierError` raised at emit time."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.quantifier import DanglingQuantifierError


def test_to_regex_string_raises_when_a_bare_quantifier_has_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().exactly(3).to_regex_string()


def test_to_regex_string_raises_for_optional_with_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().optional().to_regex_string()


def test_to_regex_string_raises_for_zero_or_more_with_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().zero_or_more().to_regex_string()


def test_to_regex_string_raises_for_one_or_more_with_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().one_or_more().to_regex_string()


def test_to_regex_string_raises_for_between_with_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().between(2, 5).to_regex_string()


def test_pattern_to_regex_string_raises_when_a_bare_quantifier_has_no_operand():
    with pytest.raises(DanglingQuantifierError):
        Pattern().exactly(3).to_regex_string()


def test_to_regex_raises_when_a_bare_quantifier_has_no_operand():
    with pytest.raises(DanglingQuantifierError):
        RegexBuilder().at_least(2).to_regex()


def test_message_hints_at_appending_an_operand():
    with pytest.raises(DanglingQuantifierError, match="Append an element"):
        RegexBuilder().exactly(3).to_regex_string()


def test_dangling_quantifier_error_message_contains_expected_text():
    error = DanglingQuantifierError()
    assert "Dangling quantifier" in str(error)
    assert "no operand" in str(error)