"""``saml`` — API-spec/protocol identifier or payload shape."""

from __future__ import annotations

from edify import Pattern

saml = (
    Pattern()
    .start_of_input()
    .between(3, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char(".")
    .char("-")
    .char("/")
    .char("+")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive saml-related identifier."""
