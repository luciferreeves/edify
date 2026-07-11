"""``saml`` — API-spec/protocol identifier or payload shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

saml = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{3,256}$")
"""Callable :class:`Pattern` for a permissive saml-related identifier."""
