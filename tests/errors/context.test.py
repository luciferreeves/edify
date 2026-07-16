"""Tests for the caller-source-location capture helpers in :mod:`edify.errors.context`."""

import linecache
from unittest import mock

from edify.errors.context import CallerContext, capture_caller_context


def test_capture_caller_context_returns_none_when_every_frame_is_inside_edify():
    with mock.patch("edify.errors.context.inspect.currentframe", return_value=None):
        assert capture_caller_context() is None


def test_caller_context_dataclass_is_frozen_and_holds_position_fields():
    context = CallerContext(filename="a.py", lineno=1, colno=1, end_colno=5)
    assert context.filename == "a.py"
    assert context.lineno == 1
    assert context.colno == 1
    assert context.end_colno == 5


def test_caller_context_source_line_property_reads_lazily_via_linecache():
    filename = "/tmp/lazy_source_test.py"
    linecache.cache[filename] = (5, None, ["x = 1\n"], filename)
    context = CallerContext(filename=filename, lineno=1, colno=1, end_colno=5)
    assert context.source_line == "x = 1"


def test_caller_context_source_line_returns_empty_string_when_line_is_unreadable():
    context = CallerContext(filename="/tmp/no_such_file.py", lineno=999, colno=1, end_colno=1)
    assert context.source_line == ""
