"""``tsv`` — tab-separated row shape."""

from __future__ import annotations

from edify import Pattern

_field = Pattern().zero_or_more().anything_but_chars("\t\r\n")

_row = Pattern().use(_field).one_or_more().group().tab().use(_field).end()

tsv = (
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
"""Callable :class:`Pattern` for tab-separated rows: at least two tab-delimited
fields per row.
"""
