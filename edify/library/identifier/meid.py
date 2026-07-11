"""``meid`` — 14-character hex Mobile Equipment Identifier."""

from __future__ import annotations

from edify import Pattern

meid = (
    Pattern()
    .start_of_input()
    .exactly(14)
    .any_of()
    .range("0", "9")
    .range("A", "F")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 14-character uppercase-hex MEID shape."""
