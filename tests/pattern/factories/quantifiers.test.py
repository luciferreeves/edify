"""Tests for the functional quantifier factories."""

import pytest

from edify import (
    DIGIT,
    WORD,
    Pattern,
    at_least,
    between,
    between_lazy,
    char,
    exactly,
    one_or_more,
    one_or_more_lazy,
    optional,
    string,
    zero_or_more,
    zero_or_more_lazy,
)
from edify.errors.input import (
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBePositiveIntegerError,
)


def test_optional_wraps_a_single_element_operand_directly():
    assert optional(char("x")).to_regex_string() == "x?"


def test_zero_or_more_wraps_a_module_constant():
    assert zero_or_more(WORD).to_regex_string() == "\\w*"


def test_zero_or_more_lazy_emits_lazy_star():
    assert zero_or_more_lazy(WORD).to_regex_string() == "\\w*?"


def test_one_or_more_wraps_a_module_constant():
    assert one_or_more(DIGIT).to_regex_string() == "\\d+"


def test_one_or_more_lazy_emits_lazy_plus():
    assert one_or_more_lazy(DIGIT).to_regex_string() == "\\d+?"


def test_exactly_wraps_a_module_constant_without_extra_grouping():
    assert exactly(3, DIGIT).to_regex_string() == "\\d{3}"


def test_exactly_groups_a_multi_element_operand():
    combined = DIGIT + WORD
    assert exactly(3, combined).to_regex_string() == "(?:\\d\\w){3}"


def test_exactly_groups_a_multi_character_string_operand():
    assert exactly(3, string("ab")).to_regex_string() == "(?:ab){3}"


def test_at_least_produces_open_ended_quantifier():
    assert at_least(2, DIGIT).to_regex_string() == "\\d{2,}"


def test_between_produces_greedy_bounded_quantifier():
    assert between(2, 4, DIGIT).to_regex_string() == "\\d{2,4}"


def test_between_lazy_produces_lazy_bounded_quantifier():
    assert between_lazy(2, 4, DIGIT).to_regex_string() == "\\d{2,4}?"


def test_optional_returns_a_pattern_instance():
    assert isinstance(optional(DIGIT), Pattern)


def test_exactly_rejects_zero_count():
    with pytest.raises(MustBePositiveIntegerError):
        exactly(0, DIGIT)


def test_at_least_rejects_negative_count():
    with pytest.raises(MustBePositiveIntegerError):
        at_least(-1, DIGIT)


def test_between_rejects_negative_lower_bound():
    with pytest.raises(MustBeIntegerGreaterThanZeroError):
        between(-1, 5, DIGIT)


def test_between_rejects_upper_bound_less_than_or_equal_to_lower():
    with pytest.raises(MustBeLessThanError):
        between(3, 3, DIGIT)
