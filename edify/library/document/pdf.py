"""``pdf`` — pdf document-format filename / marker shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
pdf = RegexBackedPattern(r"^[A-Za-z0-9_.\-/]{1,256}$")
"""Callable :class:`Pattern` for a pdf document identifier or file name."""
