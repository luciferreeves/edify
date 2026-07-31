"""``mobi`` — MOBI e-book signature shape."""

from __future__ import annotations

from edify import Pattern

mobi = (
    Pattern()
    .start_of_input()
    .exactly(60)
    .any_char()
    .string("BOOKMOBI")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a MOBI e-book: the ``BOOKMOBI`` type/creator
pair at offset 60 of the database header.
"""
