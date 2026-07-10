"""Exception classes raised when named-group operations are misused."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class NameNotValidError(EdifySyntaxError):
    """Raised when a named-group name fails the identifier shape check.

    Args:
        name: The rejected name string.
    """

    def __init__(self, name: str) -> None:
        message = compose_annotated_message(
            summary=f"named-group name {name!r} is not a valid identifier",
            trigger_hint="invalid name passed here",
            note=(
                "named-group names must be non-empty and contain only letters, digits, "
                "and underscores (no spaces, hyphens, or punctuation)."
            ),
            help_line=(
                f"help: rename {name!r} to a bare identifier "
                "(e.g. 'year', 'user_id', 'scheme')."
            ),
        )
        super().__init__(message)


class CannotCreateDuplicateNamedGroupError(EdifySyntaxError):
    """Raised when ``named_capture`` is called with a name already registered on the builder.

    Args:
        name: The duplicate name.
    """

    def __init__(self, name: str) -> None:
        message = compose_annotated_message(
            summary=f"named group {name!r} already exists in this pattern",
            trigger_hint="duplicate name declared here",
            note=(
                "every named capture group must have a unique name; the earlier "
                f".named_capture({name!r}) call already registered this one."
            ),
            help_line=(
                f"help: pick a different name for the second group, "
                f"or use .named_back_reference({name!r}) to reuse the existing group's match."
            ),
        )
        super().__init__(message)


class NamedGroupDoesNotExistError(EdifySyntaxError):
    """Raised when ``named_back_reference`` references a name that was never declared.

    Args:
        name: The name the caller tried to reference.
    """

    def __init__(self, name: str) -> None:
        message = compose_annotated_message(
            summary=f"named group {name!r} does not exist in this pattern",
            trigger_hint="unknown name referenced here",
            note=(
                f".named_back_reference({name!r}) can only refer to a group that was "
                "declared earlier in the chain; no such group has been declared yet."
            ),
            help_line=(
                f"help: add a .named_capture({name!r})...end() before this call, "
                "or reference an already-declared name."
            ),
        )
        super().__init__(message)
