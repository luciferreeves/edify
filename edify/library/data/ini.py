"""``ini`` — INI configuration shape."""

from __future__ import annotations

from edify import Pattern

_section = Pattern().char("[").one_or_more().anything_but_chars("[]\r\n").char("]")

_key = (
    Pattern()
    .any_of()
    .alphanumeric()
    .char("_")
    .end()
    .zero_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("_.- ")
    .end()
    .any_of_chars("=:")
)

_comment = Pattern().any_of_chars(";#")

ini = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_section)
    .use(_comment)
    .use(_key)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an INI file: a ``[section]`` header, a comment,
or a ``key=value`` assignment.
"""
