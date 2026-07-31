"""``toml`` — TOML document shape."""

from __future__ import annotations

from edify import Pattern

_table = (
    Pattern()
    .char("[")
    .optional()
    .char("[")
    .one_or_more()
    .anything_but_chars("[]\r\n")
    .char("]")
    .optional()
    .char("]")
)

_key = (
    Pattern()
    .any_of()
    .alphanumeric()
    .any_of_chars("_-\"'")
    .end()
    .zero_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("_.-\"'")
    .end()
    .zero_or_more()
    .whitespace_char()
    .char("=")
)

_comment = Pattern().char("#")

toml = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_table)
    .use(_comment)
    .use(_key)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a TOML document: a ``[table]`` header, a
comment, or a ``key =`` assignment.
"""
