"""``issn`` — ISSN shape (``NNNN-NNNC``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

issn = RegexBackedPattern(r"^\d{4}-\d{3}[\dXx]$")
"""Callable :class:`Pattern` for the ISSN shape."""
