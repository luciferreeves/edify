"""Exceptions raised by :mod:`edify.integrations` helpers."""

from __future__ import annotations


class PatternDidNotMatchError(ValueError):
    """Raised inside integration validators when a value fails to match the wrapped pattern.

    Inherits :class:`ValueError` so framework validation layers (pydantic, django, etc.)
    convert it into their own ``ValidationError`` shape without an extra try/except.

    Args:
        source: The regex string the value was tested against.
        value: The rejected input.
    """

    def __init__(self, source: str, value: str) -> None:
        message = (
            f"input {value!r} does not match the pattern with source {source!r}; "
            "adjust the value to match the pattern or select a pattern that accepts it."
        )
        super().__init__(message)
        self.source = source
        self.value = value
