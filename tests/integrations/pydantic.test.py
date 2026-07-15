"""Tests for :mod:`edify.integrations.pydantic`."""

import sys

import pytest

from edify import Pattern
from edify.errors.integration import MissingIntegrationDependencyError
from edify.integrations.pydantic import pattern_field, pattern_validator

_DIGITS_PATTERN = Pattern().start_of_input().one_or_more().digit().end_of_input()


def test_pattern_validator_accepts_a_matching_string_and_returns_it_unchanged():
    validate = pattern_validator(_DIGITS_PATTERN)
    assert validate("42") == "42"


def test_pattern_validator_raises_value_error_on_non_matching_input():
    validate = pattern_validator(_DIGITS_PATTERN)
    with pytest.raises(ValueError, match="does not match"):
        validate("abc")


def test_pattern_field_returns_an_annotated_str_type_for_pydantic_models():
    from typing import get_args, get_type_hints

    from pydantic import AfterValidator, BaseModel

    class Payload(BaseModel):
        value: pattern_field(_DIGITS_PATTERN)

    resolved = get_type_hints(Payload, include_extras=True)["value"]
    metadata = get_args(resolved)[1:]
    assert any(isinstance(item, AfterValidator) for item in metadata)


def test_pattern_field_is_accepted_by_pydantic_model_validation():
    from pydantic import BaseModel, ValidationError

    class Payload(BaseModel):
        value: pattern_field(_DIGITS_PATTERN)

    assert Payload(value="42").value == "42"
    with pytest.raises(ValidationError):
        Payload(value="abc")


def test_pattern_validator_raises_missing_integration_when_pydantic_absent(monkeypatch):
    monkeypatch.setitem(sys.modules, "pydantic", None)
    with pytest.raises(MissingIntegrationDependencyError, match="pydantic"):
        pattern_validator(_DIGITS_PATTERN)


def test_pattern_field_raises_missing_integration_when_pydantic_absent(monkeypatch):
    monkeypatch.setitem(sys.modules, "pydantic", None)
    with pytest.raises(MissingIntegrationDependencyError, match="pydantic"):
        pattern_field(_DIGITS_PATTERN)


def test_missing_integration_error_carries_the_actionable_install_hint(monkeypatch):
    monkeypatch.setitem(sys.modules, "pydantic", None)
    with pytest.raises(MissingIntegrationDependencyError) as excinfo:
        pattern_validator(_DIGITS_PATTERN)
    text = str(excinfo.value)
    assert "pip install edify[pydantic]" in text
    assert "= note:" in text
