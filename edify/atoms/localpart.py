"""``localpart`` — RFC 5322 email local-part shape (permissive)."""

from __future__ import annotations

from edify import Pattern

localpart = (
    Pattern()
    .between(1, 64)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("!")
    .char("#")
    .char("$")
    .char("%")
    .char("&")
    .char("'")
    .char("*")
    .char("+")
    .char("/")
    .char("=")
    .char("?")
    .char("^")
    .char("_")
    .char("`")
    .char("{")
    .char("|")
    .char("}")
    .char("~")
    .char(".")
    .char("-")
    .end()
)
"""Composable :class:`Pattern` fragment for the local part of an email address."""
