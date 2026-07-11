"""``makefile`` — Makefile-target line shape (``target: [deps]``)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
makefile = RegexBackedPattern(r"^\.?[a-zA-Z][a-zA-Z0-9._-]*(?:\s+[a-zA-Z][a-zA-Z0-9._-]*)*\s*:.*$")
"""Callable :class:`Pattern` for a Makefile-target declaration line."""
