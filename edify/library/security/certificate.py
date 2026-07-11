"""``certificate`` — certificate cryptography artifact shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
certificate = RegexBackedPattern(r"^[A-Za-z0-9+/=_\-.:\s]{16,4096}$")
"""Callable :class:`Pattern` for certificate cryptographic-artifact identifier or payload."""
