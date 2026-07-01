"""Tests for the :meth:`BuilderCore.fork` and :meth:`BuilderCore.copy` aliases."""

from edify import Pattern, RegexBuilder


def test_fork_returns_a_regex_builder_with_the_same_state():
    original = RegexBuilder().digit()
    forked = original.fork()
    assert forked == original
    assert forked is not original


def test_fork_returns_a_pattern_with_the_same_state():
    original = Pattern().word()
    forked = original.fork()
    assert forked == original
    assert forked is not original


def test_copy_returns_a_regex_builder_with_the_same_state():
    original = RegexBuilder().digit()
    copied = original.copy()
    assert copied == original
    assert copied is not original


def test_copy_returns_a_pattern_with_the_same_state():
    original = Pattern().word()
    copied = original.copy()
    assert copied == original
    assert copied is not original


def test_fork_and_copy_produce_independent_branches():
    root = RegexBuilder().digit()
    branch_a = root.fork().word()
    branch_b = root.copy().whitespace_char()
    assert root.to_regex_string() == "\\d"
    assert branch_a.to_regex_string() == "\\d\\w"
    assert branch_b.to_regex_string() == "\\d\\s"


def test_fork_and_copy_return_the_concrete_class_type():
    assert isinstance(RegexBuilder().fork(), RegexBuilder)
    assert isinstance(RegexBuilder().copy(), RegexBuilder)
    assert isinstance(Pattern().fork(), Pattern)
    assert isinstance(Pattern().copy(), Pattern)
