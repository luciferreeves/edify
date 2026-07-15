"""Tests for the validation raise paths across every builder mixin.

Each test triggers exactly one of the per-method input-validation branches
that the happy-path builder tests never hit.
"""

import pytest

from edify import RegexBuilder
from edify.errors.anchors import (
    CannotDefineStartAfterEndError,
    EndInputAlreadyDefinedError,
    StartInputAlreadyDefinedError,
)
from edify.errors.input import (
    MustBeAStringError,
    MustBeInstanceError,
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBeOneCharacterError,
    MustBePositiveIntegerError,
    MustBeSingleCharacterError,
    MustHaveASmallerValueError,
)
from edify.errors.naming import NamedGroupDoesNotExistError
from edify.errors.structure import CannotCallSubexpressionError


def test_start_of_input_twice_raises():
    with pytest.raises(StartInputAlreadyDefinedError):
        RegexBuilder().start_of_input().start_of_input()


def test_start_of_input_after_end_raises():
    with pytest.raises(CannotDefineStartAfterEndError):
        RegexBuilder().end_of_input().start_of_input()


def test_end_of_input_twice_raises():
    with pytest.raises(EndInputAlreadyDefinedError):
        RegexBuilder().end_of_input().end_of_input()


def test_named_capture_non_string_raises():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().named_capture(42)


def test_named_capture_empty_string_raises():
    with pytest.raises(MustBeOneCharacterError):
        RegexBuilder().named_capture("")


def test_string_non_string_raises():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().string(42)


def test_string_empty_raises():
    with pytest.raises(MustBeOneCharacterError):
        RegexBuilder().string("")


def test_char_non_string_raises():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().char(42)


def test_range_first_codepoint_not_less_than_second_raises():
    with pytest.raises(MustHaveASmallerValueError):
        RegexBuilder().range("z", "a")


def test_anything_but_string_non_string_raises():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().anything_but_string(42)


def test_anything_but_string_empty_raises():
    with pytest.raises(MustBeOneCharacterError):
        RegexBuilder().anything_but_string("")


def test_anything_but_chars_non_string_raises():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().anything_but_chars(42)


def test_anything_but_chars_empty_raises():
    with pytest.raises(MustBeOneCharacterError):
        RegexBuilder().anything_but_chars("")


def test_anything_but_range_multi_char_raises():
    with pytest.raises(MustBeSingleCharacterError):
        RegexBuilder().anything_but_range("abc", "z")


def test_anything_but_range_ascending_raises():
    with pytest.raises(MustHaveASmallerValueError):
        RegexBuilder().anything_but_range("z", "a")


def test_exactly_non_positive_raises():
    with pytest.raises(MustBePositiveIntegerError):
        RegexBuilder().exactly(0).digit()


def test_at_least_non_positive_raises():
    with pytest.raises(MustBePositiveIntegerError):
        RegexBuilder().at_least(-1).digit()


def test_at_most_non_positive_raises():
    with pytest.raises(MustBePositiveIntegerError):
        RegexBuilder().at_most(0).digit()


def test_between_negative_lower_raises():
    with pytest.raises(MustBeIntegerGreaterThanZeroError):
        RegexBuilder().between(-1, 5).digit()


def test_between_lower_not_less_than_upper_raises():
    with pytest.raises(MustBeLessThanError):
        RegexBuilder().between(5, 5).digit()


def test_between_lazy_negative_lower_raises():
    with pytest.raises(MustBeIntegerGreaterThanZeroError):
        RegexBuilder().between_lazy(-1, 5).digit()


def test_between_lazy_lower_not_less_than_upper_raises():
    with pytest.raises(MustBeLessThanError):
        RegexBuilder().between_lazy(5, 5).digit()


def test_named_back_reference_undeclared_raises():
    with pytest.raises(NamedGroupDoesNotExistError):
        RegexBuilder().named_back_reference("missing")


def test_to_regex_string_with_open_frame_raises():
    unfinished = RegexBuilder().capture().digit()
    with pytest.raises(CannotCallSubexpressionError):
        unfinished.to_regex_string()


def test_to_regex_with_open_frame_raises():
    unfinished = RegexBuilder().capture().digit()
    with pytest.raises(CannotCallSubexpressionError):
        unfinished.to_regex()


def test_subexpression_non_builder_raises():
    with pytest.raises(MustBeInstanceError):
        RegexBuilder().subexpression("not a builder")
