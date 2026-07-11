"""``pmc`` — PMC identifier shape (``PMCnnnnn...``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

pmc = RegexBackedPattern(r"^PMC\d{1,9}$")
"""Callable :class:`Pattern` for a PubMed Central identifier."""
