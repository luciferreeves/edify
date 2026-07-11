"""``hash`` — hex-hash digest shape (any common length)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

hash = RegexBackedPattern(r"^[a-fA-F0-9]{8,128}$")
"""Callable :class:`Pattern` for a hex-hash digest (8–128 hex characters,
covering CRC-32 through SHA-512).
"""
