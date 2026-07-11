"""``phone`` — permissive international or short-code phone-number shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

phone = RegexBackedPattern(
    r"^(?:"
    r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?"
    r"\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}"
    r"|\d{2,4}"
    r")$"
)
"""Callable :class:`Pattern` for phone-number shapes: permissive international
form (optional ``+``, country code, area code, and dash/dot/space separators)
or 2-4 digit short-code fallback.
"""
