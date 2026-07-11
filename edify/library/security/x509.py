"""``x509`` — x509 cryptography artifact shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

x509 = RegexBackedPattern(r"^[A-Za-z0-9+/=_\-.:\s]{16,4096}$")
"""Callable :class:`Pattern` for x509 cryptographic-artifact identifier or payload."""
