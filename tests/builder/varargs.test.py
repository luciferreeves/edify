"""Tests for the varargs shorthand on :meth:`GroupsMixin.any_of` and :meth:`GroupsMixin.one_of`."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.input import (
    MustBeAStringError,
    MustBeAtLeastOneLiteralError,
    MustBeOneCharacterError,
)


def test_any_of_no_args_still_opens_a_frame():
    expr = RegexBuilder().any_of().string("cat").string("dog").end()
    assert expr.to_regex_string() == "(?:cat|dog)"


def test_any_of_varargs_fuses_single_character_literals_into_a_char_class():
    expr = RegexBuilder().any_of("+", "-")
    assert expr.to_regex_string() == "[\\+\\-]"


def test_any_of_varargs_uses_alternation_for_multi_character_literals():
    expr = RegexBuilder().any_of("http", "https")
    assert expr.to_regex_string() == "(?:http|https)"


def test_any_of_varargs_returns_a_builder_of_the_same_type():
    expr = RegexBuilder().any_of("a", "b")
    assert isinstance(expr, RegexBuilder)


def test_any_of_varargs_leaves_the_original_builder_untouched():
    original = RegexBuilder().digit()
    _ = original.any_of("a", "b")
    assert original.to_regex_string() == "\\d"


def test_any_of_varargs_on_pattern_returns_a_pattern():
    pattern = Pattern().any_of("cat", "dog")
    assert isinstance(pattern, Pattern)
    assert pattern.to_regex_string() == "(?:cat|dog)"


def test_one_of_fuses_single_character_literals_into_a_char_class():
    expr = RegexBuilder().one_of("+", "-")
    assert expr.to_regex_string() == "[\\+\\-]"


def test_one_of_uses_alternation_for_multi_character_literals():
    expr = RegexBuilder().one_of("cat", "dog", "fish")
    assert expr.to_regex_string() == "(?:cat|dog|fish)"


def test_one_of_accepts_a_single_literal_and_wraps_it():
    expr = RegexBuilder().one_of("cat")
    assert expr.to_regex_string() == "(?:cat)"


def test_one_of_zero_args_raises_must_be_at_least_one_literal():
    with pytest.raises(MustBeAtLeastOneLiteralError):
        RegexBuilder().one_of()


def test_any_of_varargs_rejects_empty_string_literal():
    with pytest.raises(MustBeOneCharacterError):
        RegexBuilder().any_of("cat", "")


def test_one_of_rejects_non_string_literal():
    with pytest.raises(MustBeAStringError):
        RegexBuilder().one_of("cat", 42)
