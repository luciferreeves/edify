"""``base64url`` — URL-safe base64 string (``+`` and ``/`` replaced with ``_`` and ``-``)."""

from __future__ import annotations

from edify import Pattern

base64url = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("_")
    .char("-")
    .end()
)
"""Composable :class:`Pattern` fragment for a URL-safe base64 string."""
