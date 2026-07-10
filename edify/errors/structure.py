"""Exception classes raised for builder-frame structural errors."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class CannotEndWhileBuildingRootExpressionError(EdifySyntaxError):
    """Raised when ``.end()`` is called on a builder whose only open frame is the root."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="cannot .end() while building the root expression",
            trigger_hint=".end() called here",
            note=(
                ".end() closes the innermost open frame, but the root expression has no "
                "matching opener; there is no frame to close."
            ),
            help_line=(
                "help: remove this .end() call, or open a frame first with "
                ".capture(), .named_capture(name), .group(), .any_of(), or a lookaround."
            ),
        )
        super().__init__(message)


class CannotCallSubexpressionError(EdifySyntaxError):
    """Raised when ``.subexpression(expression)`` is given an expression with open frames.

    Args:
        current_frame_type: Name of the frame kind that is still open on the subexpression.
    """

    def __init__(self, current_frame_type: str) -> None:
        message = compose_annotated_message(
            summary="cannot merge a subexpression that has an unclosed frame",
            trigger_hint="subexpression merged here",
            note=(
                f"the subexpression still has an open {current_frame_type} frame; "
                "only fully-closed expressions can be merged into another builder."
            ),
            help_line=(
                f"help: add a matching .end() call to close the {current_frame_type} frame "
                "on the subexpression before passing it to .subexpression(...)."
            ),
        )
        super().__init__(message)
