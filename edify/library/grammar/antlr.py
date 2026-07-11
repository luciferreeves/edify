"""``antlr`` — ANTLR grammar-source shape."""

from __future__ import annotations

from edify import Pattern

antlr = (
    Pattern()
    .start_of_input()
    .string("grammar")
    .one_or_more()
    .whitespace_char()
    .letter()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("_")
    .end()
    .char(";")
    .zero_or_more()
    .any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for an ANTLR grammar source (``grammar Name;`` header + rules)."""
