"""``refresh`` — OAuth refresh-token shape (opaque, 32–512 chars)."""

from __future__ import annotations

from edify import Pattern

refresh = (
    Pattern()
    .start_of_input()
    .between(32, 512)
    .any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("._-~+/=").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an OAuth refresh-token shape: 32–512
opaque characters (URL-safe plus common padding symbols).
"""
