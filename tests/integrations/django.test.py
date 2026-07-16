"""Tests for :mod:`edify.integrations.django`."""

import pytest
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from edify import Pattern
from edify.integrations.django import pattern_validator

_DIGITS_PATTERN = Pattern().start_of_input().one_or_more().digit().end_of_input()


def test_pattern_validator_returns_a_regex_validator_pinned_to_the_pattern_source():
    validator = pattern_validator(_DIGITS_PATTERN)
    assert isinstance(validator, RegexValidator)
    assert validator.regex.pattern == _DIGITS_PATTERN.to_regex_string()


def test_pattern_validator_accepts_matching_input_without_raising():
    validator = pattern_validator(_DIGITS_PATTERN)
    validator("42")


def test_pattern_validator_raises_django_validation_error_on_non_matching_input():
    validator = pattern_validator(_DIGITS_PATTERN)
    with pytest.raises(ValidationError):
        validator("abc")


def test_pattern_validator_carries_the_default_error_message_reproducing_the_regex():
    validator = pattern_validator(_DIGITS_PATTERN)
    assert _DIGITS_PATTERN.to_regex_string() in validator.message


def test_pattern_validator_accepts_an_override_message_and_code():
    validator = pattern_validator(_DIGITS_PATTERN, message="digits only", code="bad_digits")
    assert validator.message == "digits only"
    assert validator.code == "bad_digits"
