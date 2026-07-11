"""``time`` — clock-time shape (12h/24h with optional seconds/milliseconds)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

time = RegexBackedPattern(
    r"^(?:"
    r"(?:2[0-3]|[01]?\d):[0-5]\d(?::[0-5]\d(?:\.\d{1,6})?)?"
    r"|(?:1[0-2]|0?[1-9]):[0-5]\d(?::[0-5]\d)?\s?[AaPp][Mm]"
    r")$"
)
"""Callable :class:`Pattern` for clock-time shapes: 24-hour
``HH:MM[:SS[.ffffff]]`` or 12-hour ``H:MM[:SS] AM/PM``.
"""
