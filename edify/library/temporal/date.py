"""``date`` — calendar-date shape (multiple accepted forms)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

date = RegexBackedPattern(
    r"^(?:"
    r"\d{1,2}/\d{1,2}/\d{4}"
    r"|\d{4}-\d{2}-\d{2}"
    r"|\d{2}-\d{2}-\d{4}"
    r"|\d{4}/\d{2}/\d{2}"
    r"|\d{1,2}\.\d{1,2}\.\d{4}"
    r"|\d{4}\.\d{2}\.\d{2}"
    r"|\d{8}"
    r")$"
)
"""Callable :class:`Pattern` for calendar-date shapes:
``M/D/YYYY``, ``YYYY-MM-DD``, ``DD-MM-YYYY``, ``YYYY/MM/DD``,
``DD.MM.YYYY``, ``YYYY.MM.DD``, or ``YYYYMMDD``.
"""
