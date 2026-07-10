"""Exception class raised for invalid capture-group references."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class InvalidTotalCaptureGroupsIndexError(EdifySyntaxError):
    """Raised when ``back_reference(index)`` is given an index out of range.

    Args:
        index: The 1-based index the caller requested.
        total_capture_groups: How many capture groups exist on the builder so far.
    """

    def __init__(self, index: int, total_capture_groups: int) -> None:
        if total_capture_groups == 0:
            note = (
                f"the pattern has no capture groups yet; index {index} refers to nothing."
            )
            help_line = "help: add a .capture() call before this back_reference."
        else:
            plural = "s" if total_capture_groups != 1 else ""
            note = (
                f"the pattern currently has {total_capture_groups} capture group{plural} "
                f"(valid indices are 1 to {total_capture_groups}); index {index} is out of range."
            )
            help_line = (
                f"help: use an index between 1 and {total_capture_groups}, "
                "or add another .capture() first."
            )
        message = compose_annotated_message(
            summary=f"back_reference index #{index} is out of range",
            trigger_hint=f"index {index} referenced here",
            note=note,
            help_line=help_line,
        )
        super().__init__(message)
