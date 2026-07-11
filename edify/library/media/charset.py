"""``charset`` — character set name shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

charset = RegexBackedPattern(r"^[a-zA-Z][a-zA-Z0-9_+.\-]{1,39}$")
"""Callable :class:`Pattern` for an IANA character-set name."""
