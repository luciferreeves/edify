"""Exception class raised for invalid capture-group references.

``back_reference(index)`` accepts a 1-based index that must already exist on
the builder. Passing an out-of-range index raises this error rather than
silently emitting a broken regex.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class InvalidTotalCaptureGroupsIndexError(EdifySyntaxError):
    """Raised when ``back_reference(index)`` is given an index out of range."""

    def __init__(self, index: int, total_capture_groups: int) -> None:
        message = f"Invalid index #{index}. There are only {total_capture_groups} capture groups."
        super().__init__(message)
