"""``useragent`` — User-Agent request-header shape."""

from __future__ import annotations

from edify import Pattern

useragent = (
    Pattern()
    .start_of_input()
    .between(4, 1024)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("/")
    .char(".")
    .char("-")
    .char("(")
    .char(")")
    .char(" ")
    .char(";")
    .char("+")
    .char("_")
    .char(",")
    .char(":")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive User-Agent string."""
