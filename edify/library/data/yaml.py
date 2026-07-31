"""``yaml`` — YAML document shape."""

from __future__ import annotations

from edify import Pattern

_key = (
    Pattern()
    .any_of()
    .alphanumeric()
    .any_of_chars("_\"'")
    .end()
    .zero_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("_.- \"'")
    .end()
    .char(":")
    .any_of()
    .whitespace_char()
    .end_of_input()
    .end()
)

_item = Pattern().string("- ")
_marker = Pattern().string("---")
_comment = Pattern().char("#")

yaml = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_marker)
    .use(_comment)
    .use(_item)
    .use(_key)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a YAML document: a ``---`` marker, a comment, a
``- `` sequence item, or a ``key:`` mapping.
"""
