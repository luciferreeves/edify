"""``age`` — age cryptography artifact shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
age = RegexBackedPattern(r"^[A-Za-z0-9+/=_\-.:\s]{16,4096}$")
"""Callable :class:`Pattern` for age cryptographic-artifact identifier or payload."""
