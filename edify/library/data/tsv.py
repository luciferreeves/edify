"""``tsv`` — tsv data-format / file-marker shape."""

from __future__ import annotations

from edify import Pattern

tsv = (
    Pattern()
    .start_of_input()
    .between(2, 256)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char(".")
    .char("-")
    .char("/")
    .char("+")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for tsv data-format identifier or content marker."""
