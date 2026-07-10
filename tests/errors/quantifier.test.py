"""Tests for the :mod:`edify.errors.quantifier` exception classes."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.quantifier import DanglingQuantifierError, StackedQuantifierError


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


def test_dangling_message_hints_at_appending_an_operand():
    with pytest.raises(DanglingQuantifierError, match="append the element"):
        RegexBuilder().exactly(3).to_regex_string()


def test_dangling_quantifier_error_message_contains_expected_text():
    error = DanglingQuantifierError()
    text = str(error)
    assert "dangling quantifier" in text
    assert "no operand" in text


def test_stacking_one_or_more_over_exactly_raises():
    with pytest.raises(StackedQuantifierError):
        RegexBuilder().one_or_more().exactly(3).digit()


def test_stacking_optional_over_at_least_raises():
    with pytest.raises(StackedQuantifierError):
        RegexBuilder().optional().at_least(2).digit()


def test_stacking_between_over_zero_or_more_raises():
    with pytest.raises(StackedQuantifierError):
        RegexBuilder().zero_or_more().between(1, 3).digit()


def test_stacking_lazy_variants_also_raises():
    with pytest.raises(StackedQuantifierError):
        RegexBuilder().one_or_more_lazy().exactly(2).digit()


def test_stacking_on_pattern_raises():
    with pytest.raises(StackedQuantifierError):
        Pattern().one_or_more().exactly(3).digit()


def test_a_valid_quantifier_element_quantifier_element_chain_works():
    expr = RegexBuilder().one_or_more().digit().exactly(3).word()
    assert expr.to_regex_string() == "\\d+\\w{3}"


def test_stacked_quantifier_error_message_contains_expected_text():
    error = StackedQuantifierError()
    text = str(error)
    assert "stack a quantifier" in text
    assert "pending quantifier" in text
