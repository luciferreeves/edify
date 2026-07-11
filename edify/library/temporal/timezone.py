"""``timezone`` — IANA / abbreviation timezone shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

timezone = RegexBackedPattern(
    r"^(?:"
    r"[A-Z][a-zA-Z_+\-]+(?:/[A-Z][a-zA-Z_+\-]+)+"
    r"|UTC|GMT|UT|Z"
    r"|[A-Z]{2,5}"
    r")$"
)
"""Callable :class:`Pattern` for the timezone shape:
IANA region/city (``America/Los_Angeles``), or short abbreviation
(``UTC``, ``PST``, ``EST``, …).
"""
