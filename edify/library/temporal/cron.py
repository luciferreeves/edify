"""``cron`` — cron-expression shape (5 or 6 whitespace-separated fields)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

cron = RegexBackedPattern(
    r"^(?:@(?:annually|yearly|monthly|weekly|daily|hourly|reboot)"
    r"|(?:[*?\d/,\-]+\s+){4,5}[*?\d/,\-]+)$"
)
"""Callable :class:`Pattern` for cron-expression shapes: shortcut aliases
(``@daily`` etc.) or 5-/6-field whitespace-separated expressions.
"""
