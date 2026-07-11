"""``timestamp`` — Unix millisecond timestamp shape (13-digit integer)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

timestamp = RegexBackedPattern(r"^-?\d{10,13}$")
"""Callable :class:`Pattern` for a Unix epoch timestamp in seconds or
milliseconds: optional sign followed by 10–13 digits.
"""
