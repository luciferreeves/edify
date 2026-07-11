"""``handle`` — social-media ``@name`` handle shape."""

from __future__ import annotations

from edify import Pattern

handle = (
    Pattern()
    .start_of_input()
    .char("@")
    .between(1, 30)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("_")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a social-media ``@handle`` shape."""
