"""``svg`` — SVG image document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char().string("<svg")

_root = Pattern().string("<svg")

_comment = Pattern().string("<!--").zero_or_more().any_char().string("<svg")

svg = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_declaration)
    .use(_comment)
    .use(_root)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an SVG document: an ``<svg`` root element,
optionally preceded by an XML declaration or a comment.
"""
