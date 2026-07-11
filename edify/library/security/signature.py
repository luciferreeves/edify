"""``signature`` — digital-signature payload shape (base64/hex-safe alphabet)."""

from __future__ import annotations

from edify import Pattern

signature = (
    Pattern()
    .start_of_input()
    .between(64, 4096)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("+")
    .char("/")
    .char("=")
    .char("_")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a digital-signature payload."""
