"""``ratio`` — ratio shape (``A:B`` where A and B are integers)."""

from __future__ import annotations

from edify import Pattern

ratio = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .digit()
    .char(":")
    .one_or_more()
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for a ratio shape: ``digits:digits``."""
