"""``csp`` — Content-Security-Policy directive shape."""

from __future__ import annotations

from edify import Pattern


def _directive_value() -> Pattern:
    return Pattern().assert_not_ahead().char(";").end().any_char()


csp = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .char("-")
    .end()
    .one_or_more()
    .whitespace_char()
    .one_or_more()
    .subexpression(_directive_value())
    .zero_or_more()
    .group()
    .char(";")
    .zero_or_more()
    .whitespace_char()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .char("-")
    .end()
    .one_or_more()
    .whitespace_char()
    .one_or_more()
    .subexpression(_directive_value())
    .end()
    .optional()
    .char(";")
    .end_of_input()
)
"""Callable :class:`Pattern` for a Content-Security-Policy directive shape."""
