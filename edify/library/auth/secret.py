"""``secret`` — opaque secret string shape (16-256 URL-safe chars)."""

from __future__ import annotations

from edify import Pattern

secret = (
    Pattern()
    .start_of_input()
    .between(16, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .any_of_chars("_-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an opaque secret string: 16-256 URL-safe characters."""
