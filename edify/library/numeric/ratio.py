"""``ratio`` — ratio shape (``A:B`` where A and B are integers)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

ratio = RegexBackedPattern(r"^\d+:\d+$")
"""Callable :class:`Pattern` for a ratio shape: ``digits:digits``."""
