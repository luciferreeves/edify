"""``pptx`` — presentation package signature shape."""

from __future__ import annotations

from edify import Pattern

pptx = (
    Pattern()
    .start_of_input()
    .string("PK\x03\x04")
    .zero_or_more()
    .any_char()
    .string("ppt/")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a presentation package: a ZIP container whose
entries include ``ppt/``.
"""
