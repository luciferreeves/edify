"""``rss`` — RSS feed document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

rss = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .optional()
    .use(_declaration)
    .string("<rss")
    .any_of()
    .whitespace_char()
    .char(">")
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an RSS feed: an ``<rss`` root element,
optionally preceded by an XML declaration.
"""
