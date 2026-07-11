"""``sitemap`` — sitemap web-artifact identifier/URL/content shape."""

from __future__ import annotations

from edify import Pattern

sitemap = (
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
"""Callable :class:`Pattern` for sitemap web-artifact identifier or content marker."""
