"""``pem`` — pem cryptography artifact shape."""

from __future__ import annotations

from edify import Pattern

pem = (
    Pattern()
    .start_of_input()
    .between(16, 4096)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("+")
    .char("/")
    .char("=")
    .char("_")
    .char("-")
    .char(".")
    .char(":")
    .whitespace_char()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for pem cryptographic-artifact identifier or payload."""
