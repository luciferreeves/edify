"""``barcode`` — generic barcode value shape (numeric or alphanumeric)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

barcode = RegexBackedPattern(r"^[A-Z0-9]{6,48}$")
"""Callable :class:`Pattern` for a generic barcode value shape."""
