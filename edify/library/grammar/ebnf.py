"""``ebnf`` — ebnf grammar-spec content shape."""

from __future__ import annotations

from edify import Pattern

ebnf = (
    Pattern()
    .start_of_input()
    .between(4, 65536)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char("-")
    .char("<")
    .char(">")
    .char(":")
    .char("=")
    .char("|")
    .char("*")
    .char("+")
    .char("?")
    .char("(")
    .char(")")
    .char("[")
    .char("]")
    .char("{")
    .char("}")
    .whitespace_char()
    .char(".")
    .char("'")
    .char('"')
    .char("/")
    .char(";")
    .char(",")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for ebnf grammar-specification content."""
