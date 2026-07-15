"""Exception classes raised for quantifier misuse in a builder chain."""

from __future__ import annotations

from edify.errors.context import CallerContext
from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class DanglingQuantifierError(EdifySyntaxError):
    """Raised when a terminal is called while a quantifier is still pending.

    Args:
        pending_quantifier_name: Human-readable name of the pending quantifier,
            e.g. ``"exactly(3)"`` or ``"one_or_more()"``. ``None`` when the name
            could not be recovered.
        pending_quantifier_call_site: Caller context for the chain call that queued
            the pending quantifier; ``None`` when the location could not be captured.
    """

    def __init__(
        self,
        pending_quantifier_name: str | None = None,
        pending_quantifier_call_site: CallerContext | None = None,
    ) -> None:
        summary = _format_dangling_summary(pending_quantifier_name)
        note = _format_dangling_note(pending_quantifier_name, pending_quantifier_call_site)
        message = compose_annotated_message(
            summary=summary,
            trigger_hint="terminal called here",
            note=note,
            help_line=(
                "help: append the element the quantifier should apply to "
                "(e.g. .digit(), .word(), .string('...')) before the terminal call."
            ),
        )
        super().__init__(message)
        self.pending_quantifier_name = pending_quantifier_name
        self.pending_quantifier_call_site = pending_quantifier_call_site


def _format_dangling_summary(pending_quantifier_name: str | None) -> str:
    if pending_quantifier_name is None:
        return "dangling quantifier with no operand to apply to"
    return f"dangling .{pending_quantifier_name} with no operand to apply to"


def _format_dangling_note(
    pending_quantifier_name: str | None,
    pending_quantifier_call_site: CallerContext | None,
) -> str:
    generic_prefix = (
        "a quantifier such as .exactly(n), .one_or_more(), .at_least(n), or "
        ".between(a, b) attaches to the next element in the chain; the chain "
        "ended before an element was supplied."
    )
    if pending_quantifier_name is None or pending_quantifier_call_site is None:
        return generic_prefix
    location = pending_quantifier_call_site
    return (
        f"{generic_prefix}\n"
        f"dangling quantifier: .{pending_quantifier_name} — queued at "
        f"{location.filename}:{location.lineno}:{location.colno}"
    )


class StackedQuantifierError(EdifySyntaxError):
    """Raised when a quantifier chain method is called with another quantifier already pending."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="cannot stack a quantifier on top of another pending quantifier",
            trigger_hint="second quantifier queued here",
            note=(
                "a quantifier waits for the next element in the chain; adding another "
                "quantifier before that element would leave the earlier one with nothing "
                "to attach to."
            ),
            help_line=(
                "help: add an operand (e.g. .digit(), .word()) between the two "
                "quantifier calls, or drop one of the two quantifiers."
            ),
        )
        super().__init__(message)
