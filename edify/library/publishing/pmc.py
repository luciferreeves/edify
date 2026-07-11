"""``pmc`` — PMC identifier shape (``PMCnnnnn...``)."""

from __future__ import annotations

from edify import Pattern

pmc = Pattern().start_of_input().string("PMC").between(1, 9).digit().end_of_input()
"""Callable :class:`Pattern` for a PubMed Central identifier."""
