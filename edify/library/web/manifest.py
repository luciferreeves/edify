"""``manifest`` — web application manifest shape."""

from __future__ import annotations

from edify import Pattern

manifest = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .char("{")
    .zero_or_more()
    .any_char()
    .char('"')
    .any_of()
    .string("start_url")
    .string("display")
    .string("icons")
    .string("short_name")
    .string("theme_color")
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
"""Callable :class:`Pattern` for a web application manifest: a JSON object
carrying a ``start_url``, ``display``, ``icons``, ``short_name``, or
``theme_color`` member.
"""
