"""``mpn`` — Manufacturer Part Number (permissive alphanumeric)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
mpn = RegexBackedPattern(r"^[A-Z0-9][A-Z0-9\-_.]{1,63}$")
"""Callable :class:`Pattern` for a permissive Manufacturer Part Number."""
