"""``xml`` — XML document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

_element = (
    Pattern()
    .char("<")
    .any_of()
    .letter()
    .char("_")
    .end()
    .zero_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("._-:")
    .end()
    .zero_or_more()
    .any_char()
)

xml = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_declaration)
    .use(_element)
    .end()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an XML document: an ``<?xml`` declaration or a
root element tag.
"""
