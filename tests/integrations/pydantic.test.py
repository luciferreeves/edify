"""Tests for :mod:`edify.integrations.pydantic`."""

from typing import Annotated

import pytest
from pydantic import AfterValidator, BaseModel, ValidationError

from edify import Pattern
from edify.errors.integration import PatternDidNotMatchError
from edify.integrations.pydantic import pattern_validator

_DIGITS_PATTERN = Pattern().start_of_input().one_or_more().digit().end_of_input()


def test_pattern_validator_accepts_a_matching_string_and_returns_it_unchanged():
    validate = pattern_validator(_DIGITS_PATTERN)
    assert validate("42") == "42"


def test_pattern_validator_raises_pattern_did_not_match_on_non_matching_input():
    validate = pattern_validator(_DIGITS_PATTERN)
    with pytest.raises(PatternDidNotMatchError, match="does not match"):
        validate("abc")


def test_pattern_did_not_match_error_is_a_value_error_subclass():
    assert issubclass(PatternDidNotMatchError, ValueError)


def test_pattern_did_not_match_error_carries_source_and_value():
    validate = pattern_validator(_DIGITS_PATTERN)
    with pytest.raises(PatternDidNotMatchError) as excinfo:
        validate("abc")
    assert excinfo.value.source == _DIGITS_PATTERN.to_regex_string()
    assert excinfo.value.value == "abc"


def test_pattern_validator_composes_into_pydantic_model_field_via_annotated_after_validator():
    validator_callable = pattern_validator(_DIGITS_PATTERN)

    class Payload(BaseModel):
        value: Annotated[str, AfterValidator(validator_callable)]

    assert Payload(value="42").value == "42"
    with pytest.raises(ValidationError):
        Payload(value="abc")
