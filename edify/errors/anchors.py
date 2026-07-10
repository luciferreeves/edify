"""Exception classes raised when start/end-of-input anchors are misused."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class StartInputAlreadyDefinedError(EdifySyntaxError):
    """Raised when ``start_of_input`` is added to a pattern that already has one.

    Args:
        in_subexpression: True when the duplicate came from a subexpression being merged
            into a parent that already carries the anchor.
    """

    def __init__(self, in_subexpression: bool = False) -> None:
        if in_subexpression:
            help_line = (
                "help: pass ignore_start_and_end=True when merging the subexpression "
                "so its own start_of_input is dropped."
            )
        else:
            help_line = "help: remove the duplicate .start_of_input() call from the chain."
        message = compose_annotated_message(
            summary="start_of_input has already been added to this pattern",
            trigger_hint="second start_of_input added here",
            note=(
                "a pattern can carry at most one start_of_input anchor; "
                "the earlier .start_of_input() call already set it."
            ),
            help_line=help_line,
        )
        super().__init__(message)


class CannotDefineStartAfterEndError(EdifySyntaxError):
    """Raised when ``start_of_input`` is added after ``end_of_input``."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="start_of_input cannot follow end_of_input in the chain",
            trigger_hint="start_of_input added here",
            note=(
                "start_of_input must come before any content; the pattern already declared "
                "end_of_input, so the anchor order is inverted."
            ),
            help_line="help: move .start_of_input() to before the .end_of_input() call.",
        )
        super().__init__(message)


class EndInputAlreadyDefinedError(EdifySyntaxError):
    """Raised when ``end_of_input`` is added to a pattern that already has one.

    Args:
        in_subexpression: True when the duplicate came from a subexpression being merged
            into a parent that already carries the anchor.
    """

    def __init__(self, in_subexpression: bool = False) -> None:
        if in_subexpression:
            help_line = (
                "help: pass ignore_start_and_end=True when merging the subexpression "
                "so its own end_of_input is dropped."
            )
        else:
            help_line = "help: remove the duplicate .end_of_input() call from the chain."
        message = compose_annotated_message(
            summary="end_of_input has already been added to this pattern",
            trigger_hint="second end_of_input added here",
            note=(
                "a pattern can carry at most one end_of_input anchor; "
                "the earlier .end_of_input() call already set it."
            ),
            help_line=help_line,
        )
        super().__init__(message)
