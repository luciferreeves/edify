"""``signing`` — request-signature shape (hex or base64, 32–256 chars)."""

from __future__ import annotations

from edify import Pattern

signing = (
    Pattern()
    .start_of_input()
    .between(32, 256)
    .any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("+/=_-").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a request-signature payload: 32–256
base64-family characters.
"""
