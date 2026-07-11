"""``epub`` — epub document-format filename / marker shape."""

from __future__ import annotations

from edify import Pattern

epub = (
    Pattern()
    .start_of_input()
    .between(1, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char(".")
    .char("-")
    .char("/")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a epub document identifier or file name."""
