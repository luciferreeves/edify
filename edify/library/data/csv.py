"""``csv`` — comma-separated row shape."""

from __future__ import annotations

from edify import Pattern

_field = (
    Pattern()
    .any_of()
    .subexpression(Pattern().char('"').zero_or_more().anything_but_chars('"').char('"'))
    .subexpression(Pattern().zero_or_more().anything_but_chars(',"\r\n'))
    .end()
)

_row = Pattern().use(_field).one_or_more().group().char(",").use(_field).end()

csv = (
    Pattern()
    .start_of_input()
    .use(_row)
    .zero_or_more()
    .group()
    .one_or_more()
    .any_of_chars("\r\n")
    .use(_row)
    .end()
    .zero_or_more()
    .any_of_chars("\r\n")
    .end_of_input()
)
"""Callable :class:`Pattern` for comma-separated rows: at least two fields per
row, with optional double-quoted fields.
"""
