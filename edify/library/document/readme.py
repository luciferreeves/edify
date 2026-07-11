"""``readme`` — readme document-format filename / marker shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
readme = RegexBackedPattern(r"^[A-Za-z0-9_.\-/]{1,256}$")
"""Callable :class:`Pattern` for a readme document identifier or file name."""
