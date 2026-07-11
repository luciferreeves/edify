"""``hdf5`` — hdf5 data-format / file-marker shape."""

from __future__ import annotations

from edify import Pattern

hdf5 = (
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
"""Callable :class:`Pattern` for hdf5 data-format identifier or content marker."""
