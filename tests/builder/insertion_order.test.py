"""Pinned property: character-class members preserve insertion order across calls."""

from edify import RegexBuilder


def test_any_of_chars_preserves_the_exact_insertion_order_across_runs():
    first = RegexBuilder().any_of_chars("zyxabc321").to_regex_string()
    second = RegexBuilder().any_of_chars("zyxabc321").to_regex_string()
    third = RegexBuilder().any_of_chars("zyxabc321").to_regex_string()
    assert first == second == third == "[zyxabc321]"


def test_anything_but_chars_preserves_the_exact_insertion_order_across_runs():
    first = RegexBuilder().anything_but_chars("zyxabc321").to_regex_string()
    second = RegexBuilder().anything_but_chars("zyxabc321").to_regex_string()
    assert first == second == "[^zyxabc321]"


def test_any_of_chars_preserves_duplicated_members_in_declaration_order():
    emitted = RegexBuilder().any_of_chars("aabbcc").to_regex_string()
    assert emitted == "[aabbcc]"


def test_any_of_chars_never_alphabetically_sorts_its_members():
    emitted = RegexBuilder().any_of_chars("cba").to_regex_string()
    assert emitted == "[cba]"
    assert emitted != "[abc]"
