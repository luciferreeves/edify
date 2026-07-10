"""Exception classes raised for quantifier misuse in a builder chain."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class DanglingQuantifierError(EdifySyntaxError):
    """Raised when a terminal is called while a quantifier is still pending."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="dangling quantifier with no operand to apply to",
            trigger_hint="terminal called here",
            note=(
                "a quantifier such as .exactly(n), .one_or_more(), .at_least(n), or "
                ".between(a, b) attaches to the next element in the chain; the chain "
                "ended before an element was supplied."
            ),
            help_line=(
                "help: append the element the quantifier should apply to "
                "(e.g. .digit(), .word(), .string('...')) before the terminal call."
            ),
        )
        super().__init__(message)


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
