"""``version`` — permissive dotted version string shape."""

from __future__ import annotations

from edify import Pattern

version = (
    Pattern()
    .start_of_input()
    .optional()
    .char("v")
    .one_or_more()
    .digit()
    .between(0, 3)
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .group()
    .any_of_chars("-.+")
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("-")
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive dotted version string."""
