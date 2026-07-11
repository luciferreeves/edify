"""``makefile`` — Makefile-target declaration line shape."""

from __future__ import annotations

from edify import Pattern

makefile = (
    Pattern()
    .start_of_input()
    .optional()
    .char(".")
    .letter()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("-")
    .end()
    .zero_or_more()
    .group()
    .one_or_more()
    .whitespace_char()
    .letter()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("-")
    .end()
    .end()
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for a Makefile-target declaration line."""
