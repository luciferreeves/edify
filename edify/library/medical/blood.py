"""``blood`` — ABO/Rh blood-type shape (``A+``, ``AB-``, ``O+``, etc.)."""

from __future__ import annotations

from edify import Pattern

blood = (
    Pattern()
    .start_of_input()
    .group()
    .any_of()
    .string("AB")
    .char("A")
    .char("B")
    .char("O")
    .end()
    .end()
    .any_of_chars("+-")
    .end_of_input()
)
"""Callable :class:`Pattern` for an ABO/Rh blood-type shape."""
