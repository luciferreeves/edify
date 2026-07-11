"""``glob`` — Unix glob-pattern shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
glob = RegexBackedPattern(r"^[^\x00-\x1f]*[*?[\]][^\x00-\x1f]*$")
"""Callable :class:`Pattern` for a Unix glob (must contain at least one wildcard)."""
