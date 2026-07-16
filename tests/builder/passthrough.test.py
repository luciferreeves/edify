"""Tests for the pass-through branches when subexpression anchors merge without conflict."""

import pytest

from edify import RegexBuilder
from edify.errors.structure import CannotCallSubexpressionError


def test_start_of_input_merges_into_parent_without_existing_start():
    sub = RegexBuilder().start_of_input().digit()
    parent = RegexBuilder().digit()
    pattern = parent.subexpression(sub, ignore_start_and_end=False).to_regex_string()
    assert "^" in pattern


def test_end_of_input_merges_into_parent_without_existing_end():
    sub = RegexBuilder().digit().end_of_input()
    parent = RegexBuilder().digit()
    pattern = parent.subexpression(sub, ignore_start_and_end=False).to_regex_string()
    assert "$" in pattern


def test_subexpression_called_with_unfinished_expression_raises():
    unfinished_sub = RegexBuilder().capture().digit()
    parent = RegexBuilder()
    with pytest.raises(CannotCallSubexpressionError):
        parent.subexpression(unfinished_sub)
