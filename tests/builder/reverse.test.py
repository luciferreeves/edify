"""Tests for :meth:`RegexBuilder.from_regex` — the reverse parser."""

import re

import pytest

from edify import RegexBuilder
from edify.builder.reverse import UnsupportedReverseParseError


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("hello", "hello"),
        ("a", "a"),
        (r"\d+", r"\d+"),
        (r"\d*", r"\d*"),
        (r"\d?", r"\d?"),
        (r"\d{3}", r"\d{3}"),
        (r"\d{2,5}", r"\d{2,5}"),
        (r"\d{2,}", r"\d{2,}"),
        (r"\w", r"\w"),
        (r"\W", r"\W"),
        (r"\s", r"\s"),
        (r"\S", r"\S"),
        (r"\D", r"\D"),
        ("[a-z]", "[a-z]"),
        ("[abc]", "[abc]"),
        ("^", "^"),
        ("$", "$"),
        (r"\b", r"\b"),
        (r"\B", r"\B"),
        (".", "."),
        ("(?:foo)", "foo"),
        ("(abc)", "(abc)"),
        ("(?P<name>abc)", "(?P<name>abc)"),
        ("foo|bar", "(?:foo|bar)"),
        ("(?=x)y", "(?=x)y"),
        ("(?!x)y", "(?!x)y"),
        ("(?<=x)y", "(?<=x)y"),
        ("(?<!x)y", "(?<!x)y"),
    ],
)
def test_from_regex_translates_common_constructs_faithfully(source: str, expected: str):
    builder = RegexBuilder.from_regex(source)
    assert builder.to_regex_string() == expected


@pytest.mark.parametrize(
    "source",
    [
        "hello",
        r"\d+",
        "^abc$",
        r"[a-z]+",
        "(?P<x>abc)",
        "foo|bar",
        r"(?=x)\w+",
    ],
)
def test_round_trip_compiled_regex_matches_the_same_inputs(source: str):
    original = re.compile(source)
    reversed_builder = RegexBuilder.from_regex(source)
    reversed_compiled = reversed_builder.to_regex()
    for candidate in ["", "a", "abc", "abc123", "xyz", "foo bar", "hi"]:
        assert bool(original.search(candidate)) == bool(reversed_compiled.search(candidate))


def test_from_regex_raises_for_unsupported_construct():
    with pytest.raises(UnsupportedReverseParseError):
        RegexBuilder.from_regex(r"(a)\1")


def test_from_regex_raises_for_alternation_with_non_literal_branch():
    with pytest.raises(UnsupportedReverseParseError):
        RegexBuilder.from_regex(r"a|\d+")


def test_from_regex_raises_for_unsupported_class_member_shape():
    with pytest.raises(UnsupportedReverseParseError):
        RegexBuilder.from_regex(r"[\da-z_]")


def test_from_regex_lazy_quantifier_translates_via_lazy_variants():
    builder = RegexBuilder.from_regex(r"a+?")
    assert builder.to_regex_string() == "a+?"


def test_from_regex_lazy_between_translates_via_lazy_variant():
    builder = RegexBuilder.from_regex(r"a{2,5}?")
    assert builder.to_regex_string() == "a{2,5}?"


def test_from_regex_lazy_zero_or_more_translates_via_lazy_variant():
    builder = RegexBuilder.from_regex(r"a*?")
    assert builder.to_regex_string() == "a*?"


def test_from_regex_named_group_reproduces_the_name():
    builder = RegexBuilder.from_regex("(?P<username>[a-z]+)")
    emitted = builder.to_regex_string()
    assert emitted == "(?P<username>[a-z]+)"


def test_unsupported_error_message_names_the_offending_construct():
    with pytest.raises(UnsupportedReverseParseError) as excinfo:
        RegexBuilder.from_regex(r"(a)\1")
    assert "hand-write" in str(excinfo.value)


def test_from_regex_produces_a_regexbuilder_not_a_pattern():
    builder = RegexBuilder.from_regex("abc")
    assert isinstance(builder, RegexBuilder)
