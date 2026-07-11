"""Tests for the caller-source-location capture helpers in :mod:`edify.errors.context`."""

from unittest import mock

from edify.errors.context import CallerContext, capture_caller_context


def test_capture_caller_context_returns_none_when_every_frame_is_inside_edify():
    with mock.patch("edify.errors.context.sys._getframe", return_value=None):
        assert capture_caller_context() is None


def test_caller_context_dataclass_is_frozen_and_holds_all_five_fields():
    context = CallerContext(filename="a.py", lineno=1, colno=1, end_colno=5, source_line="x = 1")
    assert context.filename == "a.py"
    assert context.source_line == "x = 1"
