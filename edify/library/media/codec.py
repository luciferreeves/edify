"""``codec`` — media codec name shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
codec = RegexBackedPattern(r"^[a-zA-Z][a-zA-Z0-9_.\-]{1,29}$")
"""Callable :class:`Pattern` for a media codec name (``h264``, ``vp9``, ``aac``, etc.)."""
