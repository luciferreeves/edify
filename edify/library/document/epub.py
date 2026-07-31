"""``epub`` — EPUB publication signature shape."""

from __future__ import annotations

from edify import Pattern

epub = (
    Pattern()
    .start_of_input()
    .string("PK\x03\x04")
    .zero_or_more()
    .any_char()
    .string("application/epub+zip")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an EPUB publication: a ZIP container declaring
the ``application/epub+zip`` media type.
"""
