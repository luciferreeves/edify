"""Tests for the module-level character-class :class:`Pattern` constants."""

import pytest

from edify import (
    ANY_CHAR,
    CARRIAGE_RETURN,
    DIGIT,
    NEW_LINE,
    NON_DIGIT,
    NON_WHITESPACE,
    NON_WORD,
    NULL_BYTE,
    TAB,
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
    ],
)
def test_character_class_constant_is_a_pattern(constant):
    assert isinstance(constant, Pattern)
