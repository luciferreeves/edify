"""``subdomain`` — DNS subdomain label shape (single label under an existing domain)."""

from __future__ import annotations

from edify import Pattern

subdomain = (
    Pattern()
    .start_of_input()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .between(0, 61)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a single DNS subdomain label (1-63 chars,
alphanumeric with optional interior hyphens).
"""
