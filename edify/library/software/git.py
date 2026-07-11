"""``git`` — git commit SHA shape (7-40 hex characters)."""

from __future__ import annotations

from edify import Pattern

git = (
    Pattern()
    .start_of_input()
    .between(7, 40)
    .any_of()
    .range("a", "f")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a git commit SHA (7-40 hex characters)."""
