"""``jsonapi`` — JSON:API document shape."""

from __future__ import annotations

from edify import Pattern

jsonapi = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .char("{")
    .zero_or_more()
    .any_char()
    .char('"')
    .any_of()
    .string("jsonapi")
    .string("data")
    .string("errors")
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
"""Callable :class:`Pattern` for a JSON:API document: a JSON object carrying a
top-level ``jsonapi``, ``data``, or ``errors`` member.
"""
