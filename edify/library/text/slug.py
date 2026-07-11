"""``slug`` — URL-safe slug shape."""

from __future__ import annotations

from edify import Pattern

slug = (
    Pattern()
    .start_of_input()
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
    .end_of_input()
)
"""Callable :class:`Pattern` for a URL-safe slug: lowercase alphanumerics
separated by single hyphens.
"""
