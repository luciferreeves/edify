"""``token`` — opaque bearer/session token shape (24-256 URL-safe chars)."""

from __future__ import annotations

from edify import Pattern

token = (
    Pattern()
    .start_of_input()
    .between(24, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .any_of_chars("_-.")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for opaque token strings: 24-256 URL-safe characters."""
