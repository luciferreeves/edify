"""``favicon`` — favicon filename/URL shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
favicon = RegexBackedPattern(r"^(?:[^\x00-\x1f/\\]+/)*favicon\.(?:ico|png|svg|gif)$")
"""Callable :class:`Pattern` for a favicon file name or URL path."""
