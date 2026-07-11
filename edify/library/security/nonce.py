"""``nonce`` — cryptographic nonce shape (base64/hex-safe alphabet)."""

from __future__ import annotations

from edify import Pattern

nonce = (
    Pattern()
    .start_of_input()
    .between(16, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("+")
    .char("/")
    .char("=")
    .char("_")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a cryptographic nonce."""
