"""``domain`` — DNS domain name shape (label.label.tld)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

domain = RegexBackedPattern(
    r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,63}$"
)
"""Callable :class:`Pattern` for the DNS domain name shape:
at least one label followed by a TLD of 2-63 letters.
"""
