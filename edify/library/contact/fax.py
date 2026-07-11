"""``fax`` — fax-number shape (same permissive form as phone)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

fax = RegexBackedPattern(
    r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?"
    r"\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
)
"""Callable :class:`Pattern` for the permissive international fax-number shape."""
