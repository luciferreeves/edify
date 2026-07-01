"""Tests for :meth:`BuilderCore.__repr__` on :class:`RegexBuilder` and :class:`Pattern`."""

from edify import Pattern, RegexBuilder
from edify.builder.core import BuilderCore


class _BareBuilder(BuilderCore):
    """A minimal :class:`BuilderCore` subclass without :class:`TerminalsMixin`."""


def test_repr_of_a_fresh_regex_builder_shows_the_empty_non_capturing_group():
    assert repr(RegexBuilder()) == "<RegexBuilder '(?:)'>"


def test_repr_of_a_fresh_pattern_shows_the_empty_non_capturing_group():
    assert repr(Pattern()) == "<Pattern '(?:)'>"


def test_repr_of_a_regex_builder_shows_the_pattern_so_far():
    builder = RegexBuilder().start_of_input().exactly(4).digit().end_of_input()
    assert repr(builder) == "<RegexBuilder '^\\\\d{4}$'>"


def test_repr_of_a_pattern_shows_the_pattern_so_far():
    pattern = Pattern().one_or_more().word()
    assert repr(pattern) == "<Pattern '\\\\w+'>"


def test_repr_of_a_builder_with_open_frames_shows_the_unclosed_marker():
    builder = RegexBuilder().any_of().string("cat")
    assert repr(builder) == "<RegexBuilder '<unclosed>'>"


def test_repr_uses_the_concrete_class_name_not_the_base():
    assert repr(RegexBuilder()).startswith("<RegexBuilder ")
    assert repr(Pattern()).startswith("<Pattern ")


def test_repr_falls_back_when_the_subclass_lacks_the_terminals_mixin():
    assert repr(_BareBuilder()) == "<_BareBuilder '<unclosed>'>"
