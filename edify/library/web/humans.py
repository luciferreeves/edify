"""``humans`` — humans.txt credits file shape."""

from __future__ import annotations

from edify import Pattern

_section = (
    Pattern()
    .string("/*")
    .zero_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars(" -_")
    .end()
    .string("*/")
)

_field = (
    Pattern()
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars(" -_")
    .end()
    .char(":")
    .zero_or_more()
    .whitespace_char()
)

_comment = Pattern().char("#")

humans = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_comment)
    .use(_section)
    .use(_field)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a humans.txt credits file: a comment, a
``/* TEAM */`` style section marker, or a ``Field: value`` line.
"""
