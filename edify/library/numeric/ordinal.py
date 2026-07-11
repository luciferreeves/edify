"""``ordinal`` — English ordinal-number shape (``1st``, ``2nd``, ``3rd``, ``4th``, ...)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

ordinal = RegexBackedPattern(r"^\d+(?:st|nd|rd|th)$")
"""Callable :class:`Pattern` for an English ordinal number."""
