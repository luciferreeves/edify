"""``extension`` — file extension shape."""

from __future__ import annotations

from edify import Pattern

extension = (
    Pattern()
    .start_of_input()
    .char(".")
    .between(1, 10)
    .alphanumeric()
    .end_of_input()
)
"""Callable :class:`Pattern` for a file extension: dot + 1-10 alphanumeric."""
