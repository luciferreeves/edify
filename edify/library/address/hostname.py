"""``hostname`` — RFC 1123 hostname shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

hostname = RegexBackedPattern(
    r"^(?=.{1,253}$)(?:[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)
"""Callable :class:`Pattern` for the RFC 1123 hostname shape."""
