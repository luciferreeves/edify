"""Exception classes raised when start/end-of-input anchors are misused.

Each anchor (``start_of_input``, ``end_of_input``) may be declared at most
once per pattern, and ``start_of_input`` may not be added after
``end_of_input``. When a subexpression carries its own anchors and merges
into a parent that already has the corresponding anchor, the raised error
also points at the ``ignore_start_and_end`` opt-out.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError

_IGNORE_START_AND_END_HINT = (
    " You can ignore a subexpression's start_of_input/end_of_input markers "
    "with the ignore_start_and_end option"
)


class StartInputAlreadyDefinedError(EdifySyntaxError):
    """Raised when ``start_of_input`` is added to a pattern that already has one."""

    def __init__(self, in_subexpression: bool = False) -> None:
        message = "Regex already has a start of input."
        if in_subexpression:
            message = message + _IGNORE_START_AND_END_HINT
        super().__init__(message)


class CannotDefineStartAfterEndError(EdifySyntaxError):
    """Raised when ``start_of_input`` is added after ``end_of_input``."""

    def __init__(self) -> None:
        message = "Can not define a start of input after defining an end of input."
        super().__init__(message)


class EndInputAlreadyDefinedError(EdifySyntaxError):
    """Raised when ``end_of_input`` is added to a pattern that already has one."""

    def __init__(self, in_subexpression: bool = False) -> None:
        message = "Regex already has an end of input."
        if in_subexpression:
            message = message + _IGNORE_START_AND_END_HINT
        super().__init__(message)
