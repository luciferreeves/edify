"""``socket`` — ``host:port`` socket address shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

socket = RegexBackedPattern(
    r"^"
    r"(?:"
    r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)"
    r"(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}"
    r"|\[[0-9a-fA-F:]+\]"
    r"|[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
    r")"
    r":\d{1,5}$"
)
"""Callable :class:`Pattern` for the ``host:port`` socket-address shape."""
