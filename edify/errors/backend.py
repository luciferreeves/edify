"""Exceptions raised at engine-dispatch time."""

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


class TimeoutNotSupportedByEngineError(EdifySyntaxError):
    """Raised when ``timeout=`` is passed to a match call on an ``engine='re'`` pattern."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="the timeout= kwarg is only supported under engine='regex'",
            trigger_hint="match/search/... called with timeout= here",
            note=(
                "the stdlib re module has no per-call timeout facility; only the "
                "third-party regex engine exposes one."
            ),
            help_line=(
                "help: re-compile the pattern with .to_regex(engine='regex') to use timeout=, "
                "or drop the kwarg."
            ),
        )
        super().__init__(message)


class VariableWidthLookbehindNotSupportedError(EdifySyntaxError):
    """Raised when ``engine='re'`` compiles a lookbehind whose body is variable-width."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary=(
                "assert_behind / assert_not_behind has a variable-width body, "
                "which the stdlib 're' engine does not accept"
            ),
            trigger_hint=".to_regex(engine='re') called here",
            note=(
                "stdlib re requires every lookbehind branch to be fixed-width, so a "
                "quantifier like +/*/?/{m,n} or a same-frame alternation with differing "
                "branch widths inside a lookbehind will fail to compile."
            ),
            help_line=(
                "help: switch to the third-party engine with .to_regex(engine='regex'), "
                "which supports variable-width lookbehind."
            ),
        )
        super().__init__(message)
