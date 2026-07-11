"""``cidr`` — CIDR-notation subnet ``address/prefix`` shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

cidr = RegexBackedPattern(
    r"^(?:"
    r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)"
    r"(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}"
    r"/(?:3[0-2]|[12]?\d)"
    r"|(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}"
    r"/(?:12[0-8]|1[01]\d|[1-9]?\d)"
    r")$"
)
"""Callable :class:`Pattern` for CIDR notation: IPv4 address + ``/0``-``/32``
or IPv6 address + ``/0``-``/128``.
"""
