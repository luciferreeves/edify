"""Tests for the :class:`Pattern` composition surface."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.input import MustBeInstanceError


def test_pattern_builds_the_same_element_tree_as_a_builder():
    pattern = Pattern().between(3, 20).word()
    builder = RegexBuilder().between(3, 20).word()
    assert pattern._state == builder._state


def test_pattern_has_no_to_regex_terminal():
    pattern = Pattern().digit()
    assert not hasattr(pattern, "to_regex")


def test_pattern_has_no_to_regex_string_terminal():
    pattern = Pattern().digit()
    assert not hasattr(pattern, "to_regex_string")


def test_pattern_supports_nested_use_composition():
    inner = Pattern().one_or_more().digit()
    outer = Pattern().string("v").use(inner)
    embedded = RegexBuilder().use(outer)
    assert embedded.to_regex_string() == "v\\d+"


def test_subexpression_still_accepts_a_pattern():
    pattern = Pattern().at_least(3).word()
    embedded = RegexBuilder().subexpression(pattern)
    assert embedded.to_regex_string() == "\\w{3,}"


def test_subexpression_rejects_non_builder_input():
    with pytest.raises(MustBeInstanceError):
        RegexBuilder().subexpression("not a pattern")
