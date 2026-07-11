"""``base`` — base16 / base32 / base58 / base64 / base64url encoded string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

base = RegexBackedPattern(
    r"^(?:"
    r"[0-9A-Fa-f]+"
    r"|[A-Z2-7]+=*"
    r"|[1-9A-HJ-NP-Za-km-z]+"
    r"|[A-Za-z0-9+/]+=*"
    r"|[A-Za-z0-9_-]+"
    r")$"
)
"""Callable :class:`Pattern` that accepts any of base16, base32, base58,
base64, or base64url encoded strings.
"""
