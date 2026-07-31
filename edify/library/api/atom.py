"""``atom`` — Atom feed document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

atom = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .optional()
    .use(_declaration)
    .string("<feed")
    .zero_or_more()
    .any_char()
    .string("http://www.w3.org/2005/Atom")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an Atom feed: a ``<feed`` root element carrying
the Atom namespace.
"""
