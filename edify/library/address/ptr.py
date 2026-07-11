"""``ptr`` — reverse-DNS PTR record shape (``d.c.b.a.in-addr.arpa`` or IPv6 nibble form)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

ptr = RegexBackedPattern(
    r"^(?:"
    r"(?:\d{1,3}\.){4}in-addr\.arpa\.?"
    r"|(?:[0-9a-fA-F]\.){32}ip6\.arpa\.?"
    r")$"
)
"""Callable :class:`Pattern` for the reverse-DNS PTR shape: IPv4
``d.c.b.a.in-addr.arpa`` or IPv6 32-nibble ``…ip6.arpa`` form.
"""
