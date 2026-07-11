"""``xlsx`` — xlsx document-format filename / marker shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

xlsx = RegexBackedPattern(r"^[A-Za-z0-9_.\-/]{1,256}$")
"""Callable :class:`Pattern` for a xlsx document identifier or file name."""
