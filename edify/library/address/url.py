"""``url`` — HTTP/HTTPS URL shape (with or without protocol)."""

from __future__ import annotations

from edify import Pattern

url = (
    Pattern()
    .start_of_input()
    .optional()
    .group()
    .string("http")
    .optional()
    .char("s")
    .string("://")
    .end()
    .optional()
    .group()
    .string("www.")
    .end()
    .between(1, 256)
    .any_of()
    .char("-")
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("@")
    .char(":")
    .char("%")
    .char(".")
    .char("_")
    .char("+")
    .char("~")
    .char("#")
    .char("=")
    .end()
    .char(".")
    .between(1, 6)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("(")
    .char(")")
    .end()
    .word_boundary()
    .zero_or_more()
    .any_of()
    .char("-")
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("(")
    .char(")")
    .char("@")
    .char(":")
    .char("%")
    .char("_")
    .char("+")
    .char(".")
    .char("~")
    .char("#")
    .char("?")
    .char("&")
    .char("/")
    .char("=")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive HTTP/HTTPS URL shape.

Guarantees:
    * Optional ``http[s]://`` scheme prefix.
    * Optional ``www.`` host prefix.
    * A dot-separated authority with a 1-6 character TLD, followed by an optional path.
    * Anchored at both ends.

Does not guarantee:
    * URI reachability, TLS certificate validity, or DNS resolution.
    * Non-HTTP schemes (``ftp:``, ``mailto:``, ``file:``) — those require dedicated
      validators.
    * Full RFC 3986 URI grammar — the pattern is deliberately permissive for the
      common web-URL shape.
"""
