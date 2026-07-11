"""``html`` — html data-format / file-marker shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

html = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{2,256}$")
"""Callable :class:`Pattern` for html data-format identifier or content marker."""
