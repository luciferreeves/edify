"""Exception classes for internal-consistency violations inside edify.

These errors should never fire under correct builder use; they exist so that
unrecognised AST shapes raise loudly with a specific class instead of slipping
through with a generic message.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class UnknownElementTypeError(EdifySyntaxError):
    """Raised when the compile dispatcher receives an element class it does not recognise."""

    def __init__(self, element_type_name: str) -> None:
        message = f"Cannot render unknown element type {element_type_name}"
        super().__init__(message)


class NonFusableElementError(EdifySyntaxError):
    """Raised when the char-class fuser is handed an element it cannot fuse."""

    def __init__(self, element_type_name: str) -> None:
        message = f"Cannot fuse element of type {element_type_name} into a char class"
        super().__init__(message)


class UnexpectedFrameTypeError(EdifySyntaxError):
    """Raised when a stack frame's anchor element is not a recognised container kind."""

    def __init__(self, element_type_name: str) -> None:
        message = f"Stack frame anchored at unexpected element type {element_type_name}"
        super().__init__(message)


class FailedToCompileRegexError(EdifySyntaxError):
    """Raised when the underlying ``re`` engine rejects the emitted pattern."""

    def __init__(self, underlying_error_message: str) -> None:
        message = f"Cannot compile regex: {underlying_error_message}"
        super().__init__(message)
