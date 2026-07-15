"""Exception classes raised when the ``engine`` kwarg selects an unavailable backend."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class EngineNotWiredError(EdifySyntaxError):
    """Raised when ``.to_regex(engine=...)`` selects a backend this build does not wire.

    Args:
        requested_engine: The value the caller passed for the ``engine`` kwarg.
    """

    def __init__(self, requested_engine: str) -> None:
        message = compose_annotated_message(
            summary=(
                f"engine={requested_engine!r} is not wired in this build; only 're' is available"
            ),
            trigger_hint=".to_regex(engine=…) called here",
            note=(
                f"the {requested_engine!r} backend is a planned optional dependency "
                "and its dispatch has not shipped yet."
            ),
            help_line=(
                "help: call .to_regex() without the engine kwarg, or pin edify to a "
                "release that wires the requested backend."
            ),
        )
        super().__init__(message)
