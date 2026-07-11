"""``pmid`` — PubMed identifier shape (1-8 digits)."""

from __future__ import annotations

from edify import Pattern

pmid = Pattern().start_of_input().between(1, 8).digit().end_of_input()
"""Callable :class:`Pattern` for a PubMed identifier (1-8 digits)."""
