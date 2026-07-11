"""``barcode`` — generic barcode value shape (numeric or alphanumeric)."""

from __future__ import annotations

from edify import Pattern

barcode = (
    Pattern()
    .start_of_input()
    .between(6, 48)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a generic barcode value shape."""
