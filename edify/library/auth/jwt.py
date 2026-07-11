"""``jwt`` — JSON Web Token shape (three base64url segments separated by dots)."""

from __future__ import annotations

from edify import Pattern

jwt = (
    Pattern()
    .start_of_input()
    .one_or_more().any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("_-").end()
    .char(".")
    .one_or_more().any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("_-").end()
    .char(".")
    .one_or_more().any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("_-").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the JWT shape: three base64url-encoded
segments separated by dots (``header.payload.signature``).
"""
