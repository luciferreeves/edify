"""``rss`` — API-spec/protocol identifier or payload shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
rss = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{3,256}$")
"""Callable :class:`Pattern` for a permissive rss-related identifier."""
