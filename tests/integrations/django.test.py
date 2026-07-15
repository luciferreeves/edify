"""Tests for :mod:`edify.integrations.django`."""

import sys

import pytest

from edify import Pattern
from edify.errors.integration import MissingIntegrationDependencyError
from edify.integrations.django import pattern_validator

_DIGITS_PATTERN = Pattern().start_of_input().one_or_more().digit().end_of_input()


def test_pattern_validator_returns_a_regex_validator_pinned_to_the_pattern_source():
    from django.core.validators import RegexValidator

    validator = pattern_validator(_DIGITS_PATTERN)
    assert isinstance(validator, RegexValidator)
    assert validator.regex.pattern == _DIGITS_PATTERN.to_regex_string()


def test_pattern_validator_accepts_matching_input_without_raising():
    validator = pattern_validator(_DIGITS_PATTERN)
    validator("42")


def test_pattern_validator_raises_django_validation_error_on_non_matching_input():
    from django.core.exceptions import ValidationError

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


def test_pattern_validator_raises_missing_integration_when_django_absent(monkeypatch):
    monkeypatch.setitem(sys.modules, "django", None)
    monkeypatch.setitem(sys.modules, "django.core", None)
    monkeypatch.setitem(sys.modules, "django.core.validators", None)
    with pytest.raises(MissingIntegrationDependencyError, match="django"):
        pattern_validator(_DIGITS_PATTERN)


def test_missing_integration_error_carries_the_actionable_install_hint(monkeypatch):
    monkeypatch.setitem(sys.modules, "django", None)
    monkeypatch.setitem(sys.modules, "django.core", None)
    monkeypatch.setitem(sys.modules, "django.core.validators", None)
    with pytest.raises(MissingIntegrationDependencyError) as excinfo:
        pattern_validator(_DIGITS_PATTERN)
    assert "pip install edify[django]" in str(excinfo.value)
