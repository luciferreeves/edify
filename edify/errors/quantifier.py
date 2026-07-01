"""Exception classes raised for quantifier misuse in a builder chain.

* :class:`DanglingQuantifierError` — a terminal was called with a pending
  quantifier that never received an operand. Emitting silently would
  drop the quantifier from the output.
* :class:`StackedQuantifierError` — a quantifier chain method was called
  while another quantifier was already pending. Emitting silently would
  drop the outer quantifier.
"""

from __future__ import annotations

from edify.errors.syntax import EdifySyntaxError


class DanglingQuantifierError(EdifySyntaxError):
    """Raised when a terminal is called while a quantifier is still pending."""

    def __init__(self) -> None:
        message = (
            "Dangling quantifier with no operand. "
            "Append an element (e.g. .digit()) before compiling."
        )
        super().__init__(message)


class StackedQuantifierError(EdifySyntaxError):
    """Raised when a quantifier chain method is called with another quantifier already pending."""

    def __init__(self) -> None:
        message = (
            "Cannot stack a quantifier on top of another pending quantifier. "
            "Add an operand between the two quantifiers or drop one."
        )
        super().__init__(message)
