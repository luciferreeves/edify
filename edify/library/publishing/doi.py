"""``doi`` — DOI shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
doi = RegexBackedPattern(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$")
"""Callable :class:`Pattern` for the DOI shape."""
