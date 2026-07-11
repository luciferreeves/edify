"""``place`` — permissive place-name / locality shape."""

from __future__ import annotations

from edify import Pattern

place = (
    Pattern()
    .start_of_input()
    .letter()
    .between(1, 99)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .char(" ")
    .char(".")
    .char(",")
    .char("'")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive place-name shape."""
