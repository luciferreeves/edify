"""``vehicle`` — vehicle/vessel/container identifier shape (permissive alphanumeric)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
vehicle = RegexBackedPattern(r"^[A-Z0-9][A-Z0-9\- ]{3,17}$")
"""Callable :class:`Pattern` for a permissive transport-vehicle identifier."""
