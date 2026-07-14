"""``slug`` — URL-safe lowercase hyphenated slug."""

from __future__ import annotations

from edify import Pattern

slug = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .end()
    .zero_or_more()
    .group()
    .char("-")
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .end()
    .end()
)
"""Composable :class:`Pattern` fragment for a URL-safe slug."""
