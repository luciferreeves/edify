"""``pmid`` — PubMed identifier shape (1-8 digits)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

pmid = RegexBackedPattern(r"^\d{1,8}$")
"""Callable :class:`Pattern` for a PubMed identifier (1-8 digits)."""
