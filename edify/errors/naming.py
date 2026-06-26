"""Exception classes raised when named-group operations are misused.

Named groups (``named_capture``, ``named_back_reference``) require a unique,
valid identifier for each name. These classes surface the three failure
modes: duplicate name, invalid name shape, and reference to a name that
was never declared.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class NameNotValidError(EdifySyntaxError):
    """Raised when a named-group name fails the identifier shape check."""

    def __init__(self, name: str) -> None:
        message = (
            f"Name {name} is not valid. (only alphanumeric characters and underscores are allowed)"
        )
        super().__init__(message)


class CannotCreateDuplicateNamedGroupError(EdifySyntaxError):
    """Raised when ``named_capture`` is called with a name already registered on the builder."""

    def __init__(self, name: str) -> None:
        message = f'Can not create duplicate named group "{name}".'
        super().__init__(message)


class NamedGroupDoesNotExistError(EdifySyntaxError):
    """Raised when ``named_back_reference`` references a name that was never declared."""

    def __init__(self, name: str) -> None:
        message = f'Named group "{name}" does not exist (create one with .named_capture()).'
        super().__init__(message)
