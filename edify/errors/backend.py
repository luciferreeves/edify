"""Exception raised when a selected engine's backend module is not installed."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class MissingRegexBackendError(EdifySyntaxError):
    """Raised when ``.to_regex(engine="regex")`` runs without the ``regex`` module installed."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="engine='regex' requires the 'regex' module, which is not installed",
            trigger_hint=".to_regex(engine='regex') called here",
            note=(
                "the 'regex' engine is an opt-in extra so pip install edify stays dependency-free."
            ),
            help_line="help: install the extra with `pip install edify[regex]` and retry.",
        )
        super().__init__(message)
