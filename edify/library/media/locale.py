"""``locale`` — POSIX/BCP-47 locale tag shape."""

from __future__ import annotations

from edify import Pattern

locale = (
    Pattern()
    .start_of_input()
    .between(2, 3)
    .lowercase()
    .optional()
    .group()
    .any_of_chars("_-")
    .exactly(2)
    .uppercase()
    .end()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .end()
    .optional()
    .group()
    .char("@")
    .one_or_more()
    .alphanumeric()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a POSIX/BCP-47 locale tag (``en``, ``en_US``, ``en-US.UTF-8``)."""
