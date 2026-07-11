"""Tests for the diagnostic helpers in :mod:`edify.builder.diagnose`."""

import pytest

from edify import Pattern, RegexBuilder
from edify.errors.comparison import CannotCompareUnfinishedBuilderError


def _first_pointer_hint(text: str) -> str | None:
    for line in text.splitlines():
        if "->" in line and ".py:" in line:
            return line
    return None


def test_two_finished_builders_compare_equal_without_diagnostic():
    left = RegexBuilder().digit()
    right = RegexBuilder().digit()
    assert left == right


def test_open_group_frame_names_group_in_the_problem_description():
    unfinished = RegexBuilder().group().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "open `group()`" in text


def test_open_capture_frame_names_capture_in_the_problem_description():
    unfinished = RegexBuilder().capture().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "open `capture()`" in text


def test_open_named_capture_frame_names_the_name_in_the_problem_description():
    unfinished = RegexBuilder().named_capture("year").digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert 'named_capture("year")' in text


def test_open_assert_ahead_frame_names_lookahead():
    unfinished = RegexBuilder().assert_ahead().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "assert_ahead()" in text


def test_open_assert_not_ahead_frame_names_negative_lookahead():
    unfinished = RegexBuilder().assert_not_ahead().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "assert_not_ahead()" in text


def test_open_assert_behind_frame_names_lookbehind():
    unfinished = RegexBuilder().assert_behind().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "assert_behind()" in text


def test_open_assert_not_behind_frame_names_negative_lookbehind():
    unfinished = RegexBuilder().assert_not_behind().digit()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished == RegexBuilder()
    text = str(excinfo.value)
    assert "assert_not_behind()" in text


def test_dangling_quantifier_on_pattern_reports_quantifier_name():
    unfinished_pattern = Pattern().one_or_more()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished_pattern == Pattern()
    text = str(excinfo.value)
    assert "pending `.one_or_more()`" in text
