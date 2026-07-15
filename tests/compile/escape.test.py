"""Tests for the character-class escape normalization.

The minimal-correct form escapes only ``\\``, ``]``, first-position ``^``,
and interior ``-`` — everything else passes through as a literal. Match
behavior against a representative corpus must stay identical to the
previous over-escaped form.
"""

import re

import pytest

from edify import RegexBuilder

_METACHARS_UNRELATED_TO_CLASS = "#?!@$%^&*"
_MIXED_CORPUS = [
    "",
    "a",
    "z",
    "#",
    "?",
    "!",
    "@",
    "$",
    "%",
    "^",
    "&",
    "*",
    "-",
    ".",
    "abc",
    "a#b",
    "1-2",
    " ",
    "foo.bar",
    "hello world",
    "a^b",
    "]",
    "[a]",
    "\\",
]


def test_any_of_chars_emits_minimal_form_for_class_safe_metachars():
    emitted = RegexBuilder().any_of_chars(_METACHARS_UNRELATED_TO_CLASS).to_regex_string()
    assert emitted == "[#?!@$%^&*]"


def test_any_of_chars_escapes_backslash_and_closing_bracket_only():
    emitted = RegexBuilder().any_of_chars("a\\b]c").to_regex_string()
    assert emitted == "[a\\\\b\\]c]"


def test_any_of_chars_escapes_first_position_caret_only():
    first_caret = RegexBuilder().any_of_chars("^abc").to_regex_string()
    later_caret = RegexBuilder().any_of_chars("a^bc").to_regex_string()
    assert first_caret == "[\\^abc]"
    assert later_caret == "[a^bc]"


def test_any_of_chars_escapes_interior_dash_only():
    edge_dashes = RegexBuilder().any_of_chars("-a-").to_regex_string()
    interior_dash = RegexBuilder().any_of_chars("a-b").to_regex_string()
    assert edge_dashes == "[-a-]"
    assert interior_dash == "[a\\-b]"


def test_any_of_chars_leaves_dot_and_asterisk_unescaped_inside_a_class():
    emitted = RegexBuilder().any_of_chars(".*").to_regex_string()
    assert emitted == "[.*]"


def test_anything_but_chars_leading_position_of_body_is_not_caret():
    emitted = RegexBuilder().anything_but_chars("^abc").to_regex_string()
    assert emitted == "[^\\^abc]"


def test_anything_but_chars_normalizes_the_same_way_as_any_of_chars():
    emitted = RegexBuilder().anything_but_chars("#?!@$%^&*").to_regex_string()
    assert emitted == "[^#?!@$%^&*]"


def test_string_terminal_still_uses_full_escape_outside_the_class():
    emitted = RegexBuilder().string("a.b").to_regex_string()
    assert emitted == "a\\.b"


def test_char_terminal_still_uses_full_escape_outside_the_class():
    emitted = RegexBuilder().char(".").to_regex_string()
    assert emitted == "\\."


@pytest.mark.parametrize("candidate", _MIXED_CORPUS)
def test_normalized_and_over_escaped_char_classes_match_the_same_inputs(candidate):
    normalized_pattern = (
        RegexBuilder().any_of_chars(_METACHARS_UNRELATED_TO_CLASS).to_regex_string()
    )
    over_escaped_pattern = f"[{re.escape(_METACHARS_UNRELATED_TO_CLASS)}]"
    normalized_hits = re.findall(normalized_pattern, candidate)
    over_escaped_hits = re.findall(over_escaped_pattern, candidate)
    assert normalized_hits == over_escaped_hits


@pytest.mark.parametrize("candidate", _MIXED_CORPUS)
def test_normalized_and_over_escaped_negated_classes_match_the_same_inputs(candidate):
    normalized_pattern = RegexBuilder().anything_but_chars("aeiou.-").to_regex_string()
    over_escaped_pattern = "[^aeiou\\.\\-]"
    normalized_hits = re.findall(normalized_pattern, candidate)
    over_escaped_hits = re.findall(over_escaped_pattern, candidate)
    assert normalized_hits == over_escaped_hits


def test_any_of_chars_empty_class_still_renders_empty():
    emitted = RegexBuilder().any_of_chars("").to_regex_string()
    assert emitted == "[]"
