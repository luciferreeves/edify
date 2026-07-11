"""``robots`` — robots web-artifact identifier/URL/content shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
robots = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+=?&#:%~]{2,4096}$")
"""Callable :class:`Pattern` for robots web-artifact identifier or content marker."""
