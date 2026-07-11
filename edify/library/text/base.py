"""``base`` — base16 / base32 / base58 / base64 / base64url encoded string shape."""

from __future__ import annotations

from edify import Pattern, any_of

_base16 = Pattern().one_or_more().any_of().range("0", "9").range("A", "F").range("a", "f").end()
_base32 = (
    Pattern().one_or_more().any_of().range("A", "Z").range("2", "7").end().zero_or_more().char("=")
)
_base58 = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("1", "9")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("a", "k")
    .range("m", "z")
    .end()
)
_base64 = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("+")
    .char("/")
    .end()
    .zero_or_more()
    .char("=")
)
_base64url = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char("-")
    .end()
)

base = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_base16, _base32, _base58, _base64, _base64url))
    .end_of_input()
)
"""Callable :class:`Pattern` that accepts any of base16, base32, base58,
base64, or base64url encoded strings.
"""
