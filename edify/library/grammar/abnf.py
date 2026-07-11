"""``abnf`` — abnf grammar-spec content shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

abnf = RegexBackedPattern(r"^[A-Za-z0-9_\-<>:=|*+?()\[\]{}\s.'\"/;,]{4,65536}$")
"""Callable :class:`Pattern` for abnf grammar-specification content."""
