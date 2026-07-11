"""``json`` — json data-format / file-marker shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

json = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{2,256}$")
"""Callable :class:`Pattern` for json data-format identifier or content marker."""
