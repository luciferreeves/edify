"""Tests for :meth:`Pattern.__call__` — validators-as-callables."""

from edify import Pattern


def test_call_returns_true_when_pattern_matches_anywhere_in_string():
    contains_digit = Pattern().digit()
    assert contains_digit("hello 42 world") is True


def test_call_returns_false_when_pattern_never_matches():
    contains_digit = Pattern().digit()
    assert contains_digit("hello world") is False


def test_call_delegates_to_test_with_search_semantics():
    only_letters = Pattern().start_of_input().one_or_more().letter().end_of_input()
    assert only_letters("abc") is True
    assert only_letters("abc123") is False


def test_call_result_is_a_bool_not_a_match_object():
    contains_digit = Pattern().digit()
    assert isinstance(contains_digit("42"), bool)


def test_call_reuses_the_cached_regex_across_repeat_calls():
    pattern = Pattern().string("hi")
    first_compiled = pattern.to_regex()
    pattern("hi world")
    pattern("bye world")
    assert pattern.to_regex() is first_compiled
