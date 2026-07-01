"""Exception classes raised when a builder method receives invalid input.

Each class is a thin :class:`EdifySyntaxError` subclass whose ``__init__``
formats the message internally. Classes that report what was passed take
the already-extracted type name as a string (``type(value).__name__``) so
the exception surface stays strongly typed end-to-end.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class MustBeAStringError(EdifySyntaxError):
    """Raised when a builder argument is required to be a string but is not."""

    def __init__(self, label: str, actual_type_name: str) -> None:
        message = f"{label} must be a string. (got {actual_type_name})"
        super().__init__(message)


class MustBeOneCharacterError(EdifySyntaxError):
    """Raised when a builder argument must have a length of at least one character."""

    def __init__(self, label: str) -> None:
        message = f"{label} must be one character long."
        super().__init__(message)


class MustBeSingleCharacterError(EdifySyntaxError):
    """Raised when a builder argument must be exactly one character long."""

    def __init__(self, label: str, actual_type_name: str) -> None:
        message = f"{label} must be a single character. (got {actual_type_name})"
        super().__init__(message)


class MustBePositiveIntegerError(EdifySyntaxError):
    """Raised when a builder argument must be a positive integer (``> 0``)."""

    def __init__(self, label: str) -> None:
        message = f"{label} must be a positive integer."
        super().__init__(message)


class MustBeIntegerGreaterThanZeroError(EdifySyntaxError):
    """Raised when a builder argument must be an integer strictly greater than zero."""

    def __init__(self, label: str) -> None:
        message = f"{label} must be an integer greater than zero."
        super().__init__(message)


class MustBeInstanceError(EdifySyntaxError):
    """Raised when a builder argument must be an instance of a specific class."""

    def __init__(self, label: str, actual_type_name: str, expected_class_name: str) -> None:
        message = f"{label} must be an instance of {expected_class_name}. (got {actual_type_name})"
        super().__init__(message)


class MustHaveASmallerValueError(EdifySyntaxError):
    """Raised when the first character argument must order before the second."""

    def __init__(self, first: str, second: str) -> None:
        first_codepoint = ord(first)
        second_codepoint = ord(second)
        message = (
            f"{first} must have a smaller character value than {second}. "
            f"(a = {first_codepoint}, b = {second_codepoint})"
        )
        super().__init__(message)


class MustBeLessThanError(EdifySyntaxError):
    """Raised when a numeric argument must order strictly before another."""

    def __init__(self, first_label: str, second_label: str) -> None:
        message = f"{first_label} must be less than {second_label}."
        super().__init__(message)


class MustBeAtLeastTwoOperandsError(EdifySyntaxError):
    """Raised when a variadic factory needs at least two operands but got fewer."""

    def __init__(self, label: str) -> None:
        message = f"{label} requires at least two operands."
        super().__init__(message)


class MustBeAtLeastOneLiteralError(EdifySyntaxError):
    """Raised when a variadic literal-alternation chain method got zero literals."""

    def __init__(self, label: str) -> None:
        message = f"{label} requires at least one literal."
        super().__init__(message)
