"""``cookie`` — HTTP cookie ``name=value`` shape."""

from __future__ import annotations

from edify import Pattern


def _value_char() -> Pattern:
    return Pattern().assert_not_ahead().any_of().whitespace_char().char(";").end().end().any_char()


cookie = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("_")
    .char("-")
    .end()
    .char("=")
    .one_or_more()
    .subexpression(_value_char())
    .end_of_input()
)
"""Callable :class:`Pattern` for an HTTP ``name=value`` cookie pair."""
