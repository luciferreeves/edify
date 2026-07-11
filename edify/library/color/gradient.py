"""``gradient`` — CSS gradient shape."""

from __future__ import annotations

from edify import Pattern

gradient = (
    Pattern()
    .start_of_input()
    .any_of("linear", "radial", "conic")
    .string("-gradient(")
    .zero_or_more()
    .anything_but_chars("()")
    .zero_or_more()
    .group()
    .char("(")
    .zero_or_more()
    .anything_but_chars("()")
    .char(")")
    .zero_or_more()
    .anything_but_chars("()")
    .end()
    .char(")")
    .end_of_input()
)
"""Callable :class:`Pattern` for a CSS gradient function call."""
