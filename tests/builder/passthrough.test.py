"""Tests for the pass-through branches when subexpression anchors merge without conflict."""

from edify import RegexBuilder


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
    import pytest

    from edify.errors.structure import CannotCallSubexpressionError

    unfinished_sub = RegexBuilder().capture().digit()
    parent = RegexBuilder()
    with pytest.raises(CannotCallSubexpressionError):
        parent.subexpression(unfinished_sub)


def test_to_regex_with_invalid_pattern_raises_failed_to_compile():
    import pytest

    from edify.errors.internal import FailedToCompileRegexError

    expr = RegexBuilder().capture().digit().end().back_reference(1)
    state_with_extra = expr._state.with_capture_groups_added(98)
    bogus = expr._with_state(state_with_extra).back_reference(99)
    with pytest.raises(FailedToCompileRegexError):
        bogus.to_regex()
