"""``challenge`` — authentication-challenge nonce shape (16-128 URL-safe chars)."""

from __future__ import annotations

from edify import Pattern

challenge = (
    Pattern()
    .start_of_input()
    .between(16, 128)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .any_of_chars("_-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an authentication challenge / nonce:
16-128 URL-safe characters.
"""
