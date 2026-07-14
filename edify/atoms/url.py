"""``url`` — permissive HTTP/HTTPS URL shape."""

from __future__ import annotations

from edify import Pattern

url = (
    Pattern()
    .string("http")
    .optional()
    .char("s")
    .string("://")
    .one_or_more()
    .anything_but_chars(" \t\r\n")
)
"""Composable :class:`Pattern` fragment for an HTTP/HTTPS URL."""
