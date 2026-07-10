"""Tests for the diagnostic helpers in :mod:`edify.builder.diagnose`."""

from types import SimpleNamespace

import pytest

from edify import Pattern, RegexBuilder
from edify.builder.diagnose import _fallback, _frame_display_name, diagnose_unfinished
from edify.errors.comparison import CannotCompareUnfinishedBuilderError


def _first_pointer_hint(text: str) -> str | None:
    for line in text.splitlines():
        if "->" in line and ".py:" in line:
            return line
    return None


def test_diagnose_returns_none_when_state_is_fully_specified():
    finished = RegexBuilder().digit()
    problem = diagnose_unfinished(finished._state, "left operand")
    assert problem is None


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


def test_frame_display_name_falls_back_to_class_name_for_unknown_container():
    mystery_class = type("MysteryContainer", (), {})
    mystery_element = mystery_class()
    fake_frame = SimpleNamespace(type_node=mystery_element)
    assert _frame_display_name(fake_frame) == "MysteryContainer"


def test_fallback_returns_context_when_provided():
    dummy_context = "sentinel"
    assert _fallback(dummy_context) == "sentinel"


def test_fallback_returns_placeholder_when_context_is_none():
    placeholder = _fallback(None)
    assert placeholder.filename == "<unknown>"
    assert placeholder.lineno == 0
    assert placeholder.source_line == ""


def test_dangling_quantifier_on_pattern_reports_quantifier_name():
    unfinished_pattern = Pattern().one_or_more()
    with pytest.raises(CannotCompareUnfinishedBuilderError) as excinfo:
        _ = unfinished_pattern == Pattern()
    text = str(excinfo.value)
    assert "pending `.one_or_more()`" in text
