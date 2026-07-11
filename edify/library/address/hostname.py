"""``hostname`` — RFC 1123 hostname shape."""

from __future__ import annotations

from edify import END, Pattern

_label_tail = (
    Pattern()
    .optional()
    .group()
    .at_most(61)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .alphanumeric()
    .end()
)

hostname = (
    Pattern()
    .start_of_input()
    .assert_ahead()
    .between(1, 253)
    .any_char()
    .subexpression(END, ignore_start_and_end=False)
    .end()
    .group()
    .alphanumeric()
    .subexpression(_label_tail)
    .end()
    .zero_or_more()
    .group()
    .char(".")
    .alphanumeric()
    .subexpression(_label_tail)
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the RFC 1123 hostname shape."""
