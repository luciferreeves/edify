"""``hal`` — API-spec/protocol identifier or payload shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

hal = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{3,256}$")
"""Callable :class:`Pattern` for a permissive hal-related identifier."""
