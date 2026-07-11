"""``rtf`` — Rich Text Format signature shape."""

from __future__ import annotations

from edify import Pattern

rtf = (
    Pattern()
    .start_of_input()
    .string("{\\rtf")
    .optional()
    .digit()
    .zero_or_more()
    .any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for an RTF document (``{\\rtfN`` prefix)."""
