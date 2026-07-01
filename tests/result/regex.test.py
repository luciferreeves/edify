"""Tests for the :class:`edify.result.Regex` wrapper class."""

import re

import pytest

from edify.result import Regex


@pytest.fixture
def digit_regex() -> Regex:
    return Regex("\\d+", re.compile("\\d+"))


def test_source_returns_the_pattern_string(digit_regex):
    assert digit_regex.source == "\\d+"


def test_compiled_returns_the_underlying_re_pattern(digit_regex):
    assert isinstance(digit_regex.compiled, re.Pattern)


def test_compiled_pattern_matches_the_source(digit_regex):
    assert digit_regex.compiled.pattern == "\\d+"


def test_match_delegates_to_the_compiled_pattern(digit_regex):
    hit = digit_regex.match("123")
    assert hit is not None
    assert hit.group() == "123"


def test_search_delegates_to_the_compiled_pattern(digit_regex):
    hit = digit_regex.search("abc 456 def")
    assert hit is not None
    assert hit.group() == "456"


def test_fullmatch_delegates_to_the_compiled_pattern(digit_regex):
    assert digit_regex.fullmatch("789") is not None
    assert digit_regex.fullmatch("7x9") is None


def test_findall_delegates_to_the_compiled_pattern(digit_regex):
    assert digit_regex.findall("1 2 3") == ["1", "2", "3"]


def test_finditer_delegates_to_the_compiled_pattern(digit_regex):
    hits = list(digit_regex.finditer("42 99"))
    assert [match.group() for match in hits] == ["42", "99"]


def test_sub_delegates_to_the_compiled_pattern(digit_regex):
    assert digit_regex.sub("[X]", "hi 12 there 34") == "hi [X] there [X]"


def test_subn_delegates_to_the_compiled_pattern(digit_regex):
    result, count = digit_regex.subn("[X]", "1 2 3")
    assert result == "[X] [X] [X]"
    assert count == 3


def test_split_delegates_to_the_compiled_pattern(digit_regex):
    assert digit_regex.split("hi1there2end") == ["hi", "there", "end"]


def test_repr_shows_the_source(digit_regex):
    assert repr(digit_regex) == "<Regex '\\\\d+'>"


def test_equal_when_source_and_flags_match():
    a = Regex("\\d+", re.compile("\\d+"))
    b = Regex("\\d+", re.compile("\\d+"))
    assert a == b


def test_not_equal_when_source_differs():
    a = Regex("\\d+", re.compile("\\d+"))
    b = Regex("\\w+", re.compile("\\w+"))
    assert a != b


def test_not_equal_when_flags_differ():
    a = Regex("\\d+", re.compile("\\d+"))
    b = Regex("\\d+", re.compile("\\d+", flags=re.IGNORECASE))
    assert a != b


def test_hash_matches_when_equal():
    a = Regex("\\d+", re.compile("\\d+"))
    b = Regex("\\d+", re.compile("\\d+"))
    assert hash(a) == hash(b)


def test_equality_with_non_regex_returns_not_implemented():
    a = Regex("\\d+", re.compile("\\d+"))
    assert a.__eq__("foo") is NotImplemented