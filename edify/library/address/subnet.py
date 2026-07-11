"""``subnet`` — dotted-decimal IPv4 subnet mask shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

subnet = RegexBackedPattern(
    r"^(?:255|254|252|248|240|224|192|128|0)\."
    r"(?:255|254|252|248|240|224|192|128|0)\."
    r"(?:255|254|252|248|240|224|192|128|0)\."
    r"(?:255|254|252|248|240|224|192|128|0)$"
)
"""Callable :class:`Pattern` for a dotted-decimal IPv4 subnet mask
(each octet is one of ``255``, ``254``, ``252``, …, ``128``, ``0``).
"""
