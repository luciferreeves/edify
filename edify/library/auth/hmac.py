"""``hmac`` — HMAC signature shape (hex digest, 32–128 chars)."""

from __future__ import annotations

from edify import Pattern

hmac = (
    Pattern()
    .start_of_input()
    .between(32, 128).any_of().range("0", "9").range("a", "f").range("A", "F").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a hex HMAC digest: 32–128 hex characters."""
