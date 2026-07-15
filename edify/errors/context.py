"""Caller-source-location capture for :mod:`edify.errors`."""

from __future__ import annotations

import linecache
import os
import sys
from dataclasses import dataclass
from types import FrameType

_EDIFY_PACKAGE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_EDIFY_PACKAGE_PREFIX = _EDIFY_PACKAGE_ROOT + os.sep


@dataclass(frozen=True)
class CallerContext:
    """A source-location snapshot of a specific call in the caller's code.

    Attributes:
        filename: Absolute path to the file that contains the offending call.
        lineno: 1-indexed line number of the offending call.
        colno: 1-indexed column at which the offending call starts.
        end_colno: 1-indexed column one past where the offending call ends.
        source_line: The verbatim source line, trailing whitespace stripped.
    """

    filename: str
    lineno: int
    colno: int
    end_colno: int
    source_line: str


def capture_caller_context() -> CallerContext | None:
    """Return a :class:`CallerContext` for the first non-``edify`` frame on the stack.

    Returns ``None`` when every frame on the stack lives inside the ``edify/``
    package tree.
    """
    current_frame: FrameType | None = sys._getframe(1)
    while current_frame is not None:
        filename = current_frame.f_code.co_filename
        absolute_filename = (
            os.path.abspath(filename) if os.path.isabs(filename) is False else filename
        )
        if not absolute_filename.startswith(_EDIFY_PACKAGE_PREFIX):
            return _context_for_frame(current_frame)
        current_frame = current_frame.f_back
    return None


def _context_for_frame(frame: FrameType) -> CallerContext:
    """Return a :class:`CallerContext` describing ``frame``'s current instruction."""
    filename = frame.f_code.co_filename
    positions = list(frame.f_code.co_positions())
    instruction_index = frame.f_lasti // 2
    raw_start_line, _end_line, raw_start_col, raw_end_col = positions[instruction_index]
    resolved_start_line = raw_start_line if raw_start_line is not None else frame.f_lineno
    resolved_start_col = raw_start_col if raw_start_col is not None else 0
    resolved_end_col = raw_end_col if raw_end_col is not None else resolved_start_col
    source_line = _read_source_line(filename, resolved_start_line)
    return CallerContext(
        filename=filename,
        lineno=resolved_start_line,
        colno=resolved_start_col + 1,
        end_colno=resolved_end_col + 1,
        source_line=source_line,
    )


def _read_source_line(filename: str, lineno: int) -> str:
    """Return the verbatim source line at ``lineno``, or an empty string when unreadable."""
    raw_line = linecache.getline(filename, lineno)
    return raw_line.rstrip()
