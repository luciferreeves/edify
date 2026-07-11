"""``humans`` — humans web-artifact identifier/URL/content shape."""

from __future__ import annotations

from edify import Pattern

humans = (
    Pattern()
    .start_of_input()
    .between(2, 4096)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char(".")
    .char("-")
    .char("/")
    .char("+")
    .char("=")
    .char("?")
    .char("&")
    .char("#")
    .char(":")
    .char("%")
    .char("~")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for humans web-artifact identifier or content marker."""
