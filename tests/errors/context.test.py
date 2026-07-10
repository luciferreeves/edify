"""Tests for the caller-source-location capture helpers in :mod:`edify.errors.context`."""

from unittest import mock

from edify.errors.context import (
    CallerContext,
    _context_for_frame,
    capture_caller_context,
)


class _FakeCode:
    """A stand-in for ``types.CodeType`` used to force specific ``co_positions`` behaviour."""

    def __init__(self, filename: str, positions: list[tuple]) -> None:
        self.co_filename = filename
        self._positions = list(positions)

    def co_positions(self):
        return iter(self._positions)


class _FakeFrame:
    """A stand-in for ``types.FrameType`` shaped for :func:`_context_for_frame`."""

    def __init__(
        self,
        filename: str,
        f_lineno: int,
        f_lasti: int,
        positions: list[tuple],
    ) -> None:
        self.f_code = _FakeCode(filename, positions)
        self.f_lineno = f_lineno
        self.f_lasti = f_lasti


def test_capture_caller_context_returns_none_when_every_frame_is_inside_edify():
    with mock.patch("edify.errors.context.sys._getframe", return_value=None):
        assert capture_caller_context() is None


def test_context_for_frame_uses_lineno_fallback_when_instruction_index_out_of_range():
    frame = _FakeFrame(
        filename="/tmp/fake.py",
        f_lineno=42,
        f_lasti=999,
        positions=[],
    )
    context = _context_for_frame(frame)
    assert context.lineno == 42
    assert context.colno == 1
    assert context.end_colno == 1


def test_context_for_frame_defaults_start_line_when_position_start_line_is_none():
    frame = _FakeFrame(
        filename="/tmp/fake.py",
        f_lineno=99,
        f_lasti=0,
        positions=[(None, None, None, None)],
    )
    context = _context_for_frame(frame)
    assert context.lineno == 99


def test_context_for_frame_defaults_end_line_when_position_end_line_is_none():
    frame = _FakeFrame(
        filename="/tmp/fake.py",
        f_lineno=7,
        f_lasti=0,
        positions=[(5, None, 2, 4)],
    )
    context = _context_for_frame(frame)
    assert context.lineno == 5
    assert context.colno == 3
    assert context.end_colno == 5


def test_context_for_frame_defaults_start_col_when_position_start_col_is_none():
    frame = _FakeFrame(
        filename="/tmp/fake.py",
        f_lineno=1,
        f_lasti=0,
        positions=[(1, 1, None, 5)],
    )
    context = _context_for_frame(frame)
    assert context.colno == 1
    assert context.end_colno == 6


def test_context_for_frame_defaults_end_col_when_position_end_col_is_none():
    frame = _FakeFrame(
        filename="/tmp/fake.py",
        f_lineno=1,
        f_lasti=0,
        positions=[(1, 1, 3, None)],
    )
    context = _context_for_frame(frame)
    assert context.colno == 4
    assert context.end_colno == 4


def test_caller_context_dataclass_is_frozen_and_holds_all_five_fields():
    context = CallerContext(filename="a.py", lineno=1, colno=1, end_colno=5, source_line="x = 1")
    assert context.filename == "a.py"
    assert context.source_line == "x = 1"
