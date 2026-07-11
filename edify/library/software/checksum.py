"""``checksum`` — hex checksum shape (CRC through SHA)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
checksum = RegexBackedPattern(r"^[a-fA-F0-9]{8,128}$")
"""Callable :class:`Pattern` for a hex checksum (any common hash width)."""
