"""Tests for the functional value factories."""

import pytest

from edify import Pattern, char, chars, nonchars, nonrange, nonstring, range_of, string
from edify.errors.input import (
    MustBeAStringError,
    MustBeOneCharacterError,
    MustBeSingleCharacterError,
    MustHaveASmallerValueError,
)


def test_string_produces_the_literal_value():
    assert string("hello").to_regex_string() == "hello"


def test_string_returns_a_pattern_instance():
    assert isinstance(string("x"), Pattern)


def test_string_escapes_regex_metacharacters():
    assert string("a.b").to_regex_string() == "a\\.b"


def test_char_produces_a_single_character_literal():
    assert char("a").to_regex_string() == "a"


def test_char_rejects_multi_character_input():
    with pytest.raises(MustBeSingleCharacterError):
        char("ab")


def test_range_of_produces_an_ascii_range():
    assert range_of("a", "z").to_regex_string() == "[a-z]"


def test_range_of_rejects_descending_bounds():
    with pytest.raises(MustHaveASmallerValueError):
        range_of("z", "a")


def test_chars_produces_an_inline_character_class():
    assert chars("abc").to_regex_string() == "[abc]"


def test_nonchars_produces_a_negated_character_class():
    assert nonchars("abc").to_regex_string() == "[^abc]"


def test_nonstring_produces_a_per_character_negation():
    assert nonstring("ab").to_regex_string() == "(?:[^a][^b])"


def test_nonrange_produces_a_negated_character_range():
    assert nonrange("a", "z").to_regex_string() == "[^a-z]"


def test_string_rejects_empty_input():
    with pytest.raises(MustBeOneCharacterError):
        string("")


def test_string_rejects_non_string_input():
    with pytest.raises(MustBeAStringError):
        string(42)
