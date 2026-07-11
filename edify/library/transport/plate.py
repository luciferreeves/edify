"""``plate`` — vehicle license-plate shape (permissive alphanumeric)."""

from __future__ import annotations

from edify import Pattern

plate = (
    Pattern()
    .start_of_input()
    .between(1, 3)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .optional()
    .any_of_chars("- ")
    .between(1, 4)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a vehicle license-plate shape."""
