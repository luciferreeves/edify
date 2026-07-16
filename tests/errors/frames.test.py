"""Tests for the structured open-frame stack surfaced by CannotCallSubexpressionError."""

import pytest

from edify import RegexBuilder
from edify.errors.quantifier import DanglingQuantifierError
from edify.errors.structure import CannotCallSubexpressionError


def test_single_open_capture_frame_is_named_in_the_error_message():
    unfinished = RegexBuilder().capture().digit()
    with pytest.raises(CannotCallSubexpressionError) as excinfo:
        unfinished.to_regex_string()
    text = str(excinfo.value)
    assert "1 open frame" in text
    assert "1. .capture()" in text


def test_nested_open_frames_are_listed_innermost_first():
    unfinished = RegexBuilder().capture().group().assert_ahead().digit()
    with pytest.raises(CannotCallSubexpressionError) as excinfo:
        unfinished.to_regex_string()
    text = str(excinfo.value)
    assert "3 open frame" in text
    innermost_index = text.index("1. .assert_ahead()")
    middle_index = text.index("2. .group()")
    outermost_index = text.index("3. .capture()")
    assert innermost_index < middle_index < outermost_index


def test_named_capture_frame_reports_the_declared_group_name():
    unfinished = RegexBuilder().named_capture("username").letter()
    with pytest.raises(CannotCallSubexpressionError) as excinfo:
        unfinished.to_regex_string()
    text = str(excinfo.value)
    assert '.named_capture("username")' in text


def test_open_frames_carry_a_file_line_column_pointer_when_the_context_is_captured():
    unfinished = RegexBuilder().assert_behind().digit()
    with pytest.raises(CannotCallSubexpressionError) as excinfo:
        unfinished.to_regex_string()
    text = str(excinfo.value)
    assert "opened at" in text
    assert __file__ in text or "frames.test.py" in text


def test_subexpression_lists_open_frames_from_the_argument_not_the_receiver():
    unfinished = RegexBuilder().named_capture("group").digit()
    parent = RegexBuilder()
    with pytest.raises(CannotCallSubexpressionError) as excinfo:
        parent.subexpression(unfinished)
    assert 'named_capture("group")' in str(excinfo.value)


def test_dangling_quantifier_reports_the_specific_pending_quantifier_name():
    with pytest.raises(DanglingQuantifierError) as excinfo:
        RegexBuilder().exactly(3).to_regex_string()
    text = str(excinfo.value)
    assert ".exactly(3)" in text


def test_dangling_quantifier_falls_back_to_generic_summary_when_name_unknown():
    error = DanglingQuantifierError()
    text = str(error)
    assert "dangling quantifier" in text
