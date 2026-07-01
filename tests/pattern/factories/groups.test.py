"""Tests for the functional grouping, capture, back-reference, and alternation factories."""

import pytest

from edify import (
    DIGIT,
    WORD,
    Pattern,
    any_of,
    back_reference,
    capture,
    group,
    named_back_reference,
    named_capture,
    string,
)
from edify.errors.input import MustBeAtLeastTwoOperandsError, MustBePositiveIntegerError


def test_group_wraps_operand_in_a_non_capturing_group():
    assert group(DIGIT + WORD).to_regex_string() == "(?:\\d\\w)"


def test_capture_wraps_operand_in_a_numbered_group():
    assert capture(DIGIT).to_regex_string() == "(\\d)"


def test_named_capture_wraps_operand_with_the_supplied_name():
    assert named_capture("year", DIGIT).to_regex_string() == "(?P<year>\\d)"


def test_back_reference_emits_a_numbered_backref():
    assert back_reference(1).to_regex_string() == "\\1"


def test_named_back_reference_emits_a_named_backref():
    assert named_back_reference("year").to_regex_string() == "(?P=year)"


def test_any_of_produces_alternation_between_multi_character_operands():
    assert any_of(string("http"), string("https")).to_regex_string() == "(?:http|https)"


def test_any_of_accepts_more_than_two_operands():
    assert any_of(string("cat"), string("dog"), string("fish")).to_regex_string() == (
        "(?:cat|dog|fish)"
    )


def test_group_returns_a_pattern_instance():
    assert isinstance(group(DIGIT), Pattern)


def test_any_of_rejects_a_single_operand():
    with pytest.raises(MustBeAtLeastTwoOperandsError):
        any_of(DIGIT)


def test_any_of_rejects_zero_operands():
    with pytest.raises(MustBeAtLeastTwoOperandsError):
        any_of()


def test_back_reference_rejects_zero_index():
    with pytest.raises(MustBePositiveIntegerError):
        back_reference(0)


def test_back_reference_rejects_negative_index():
    with pytest.raises(MustBePositiveIntegerError):
        back_reference(-1)
