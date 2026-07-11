"""``epoch`` — Unix epoch seconds shape (10-digit integer, allow negative)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

epoch = RegexBackedPattern(r"^-?\d{1,10}$")
"""Callable :class:`Pattern` for a Unix epoch-seconds value: optional sign
followed by 1–10 digits (fits in a 32-bit signed integer).
"""
