"""``pdf`` — PDF document signature shape."""

from __future__ import annotations

from edify import Pattern

pdf = (
    Pattern()
    .start_of_input()
    .string("%PDF-")
    .digit()
    .char(".")
    .digit()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a PDF document (``%PDF-1.x`` header)."""
