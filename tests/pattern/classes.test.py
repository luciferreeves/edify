"""Tests for the module-level character-class :class:`Pattern` constants."""

import pytest

from edify import (
    ALPHANUMERIC,
    ANY_CHAR,
    CARRIAGE_RETURN,
    DIGIT,
    LETTER,
    LOWERCASE,
    NEW_LINE,
    NON_DIGIT,
    NON_WHITESPACE,
    NON_WORD,
    NULL_BYTE,
    TAB,
    UPPERCASE,
    WHITESPACE,
    WORD,
    Pattern,
)


@pytest.mark.parametrize(
    ("constant", "expected"),
    [
        (ANY_CHAR, "."),
        (WHITESPACE, "\\s"),
        (NON_WHITESPACE, "\\S"),
        (DIGIT, "\\d"),
        (NON_DIGIT, "\\D"),
        (WORD, "\\w"),
        (NON_WORD, "\\W"),
        (NEW_LINE, "\\n"),
        (CARRIAGE_RETURN, "\\r"),
        (TAB, "\\t"),
        (NULL_BYTE, "\\0"),
        (LETTER, "[a-zA-Z]"),
        (UPPERCASE, "[A-Z]"),
        (LOWERCASE, "[a-z]"),
        (ALPHANUMERIC, "[a-zA-Z0-9]"),
    ],
)
def test_character_class_constant_compiles_to_expected_regex(constant, expected):
    assert constant.to_regex_string() == expected


@pytest.mark.parametrize(
    "constant",
    [
        ANY_CHAR,
        WHITESPACE,
        NON_WHITESPACE,
        DIGIT,
        NON_DIGIT,
        WORD,
        NON_WORD,
        NEW_LINE,
        CARRIAGE_RETURN,
        TAB,
        NULL_BYTE,
        LETTER,
        UPPERCASE,
        LOWERCASE,
        ALPHANUMERIC,
    ],
)
def test_character_class_constant_is_a_pattern(constant):
    assert isinstance(constant, Pattern)


@pytest.mark.parametrize(
    ("constant", "hit_input", "miss_input"),
    [
        (LETTER, "A", "4"),
        (LETTER, "z", " "),
        (UPPERCASE, "Q", "q"),
        (LOWERCASE, "q", "Q"),
        (ALPHANUMERIC, "4", " "),
        (ALPHANUMERIC, "A", "!"),
    ],
)
def test_convenience_char_class_constant_matches_expected_characters(
    constant, hit_input, miss_input
):
    assert constant.test(hit_input) is True
    assert constant.test(miss_input) is False
