"""``xlsx`` — spreadsheet package signature shape."""

from __future__ import annotations

from edify import Pattern

xlsx = (
    Pattern()
    .start_of_input()
    .string("PK\x03\x04")
    .zero_or_more()
    .any_char()
    .string("xl/")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a spreadsheet package: a ZIP container whose
entries include ``xl/``.
"""
