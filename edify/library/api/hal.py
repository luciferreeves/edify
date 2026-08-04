"""``hal`` — hypertext application language document shape."""

from __future__ import annotations

from edify import Pattern

hal = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .char("{")
    .zero_or_more()
    .any_char()
    .char('"')
    .any_of()
    .string("_links")
    .string("_embedded")
    .end()
    .char('"')
    .zero_or_more()
    .whitespace_char()
    .char(":")
    .zero_or_more()
    .any_char()
    .char("}")
    .zero_or_more()
    .whitespace_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a hypertext application language document: a
JSON object carrying a ``_links`` or ``_embedded`` member.
"""
