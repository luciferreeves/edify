"""``vehicle`` — vehicle/vessel/container identifier shape (permissive alphanumeric)."""

from __future__ import annotations

from edify import Pattern

vehicle = (
    Pattern()
    .start_of_input()
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .between(3, 17)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .char(" ")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive transport-vehicle identifier."""
