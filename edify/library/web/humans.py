"""``humans`` — humans web-artifact identifier/URL/content shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
humans = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+=?&#:%~]{2,4096}$")
"""Callable :class:`Pattern` for humans web-artifact identifier or content marker."""
