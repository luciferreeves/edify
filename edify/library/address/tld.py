"""``tld`` — top-level domain shape (2-63 alpha)."""

from __future__ import annotations

from edify import Pattern

tld = (
    Pattern()
    .start_of_input()
    .between(2, 63)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the TLD shape: 2 to 63 letters."""
