"""``pest`` — pest parser grammar shape."""

from __future__ import annotations

from edify import Pattern

_name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("_").end()

pest = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .use(_name)
    .zero_or_more()
    .any_of_chars(" \t")
    .char("=")
    .zero_or_more()
    .any_of_chars(" \t")
    .optional()
    .any_of_chars("_@$!")
    .char("{")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a pest parser grammar: a rule name, ``=``, and
a brace-delimited body with an optional silent/atomic modifier.
"""
