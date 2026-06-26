"""Exception classes raised for builder-frame structural errors.

These cover frame-stack misuse: closing the root frame, or calling
``subexpression`` on a builder whose own chain still has an open frame.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class CannotEndWhileBuildingRootExpressionError(EdifySyntaxError):
    """Raised when ``.end()`` is called on a builder whose only open frame is the root."""

    def __init__(self) -> None:
        message = "Can not end while building the root expression."
        super().__init__(message)


class CannotCallSubexpressionError(EdifySyntaxError):
    """Raised when ``.subexpression(expression)`` is given an expression with open frames."""

    def __init__(self, current_frame_type: str) -> None:
        message = (
            "Can not call subexpression on a not yet fully specified regex object. "
            f"(Try adding a .end() call to match the {current_frame_type} on the subexpression)"
        )
        super().__init__(message)
