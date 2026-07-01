"""Tests for :class:`StackedQuantifierError` raised on stacked quantifier chain calls."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.quantifier import StackedQuantifierError


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
    assert "stack" in str(error)
    assert "pending" in str(error)