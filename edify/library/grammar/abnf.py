"""``abnf`` — augmented Backus-Naur form grammar shape."""

from __future__ import annotations

from edify import Pattern

_name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("-").end()

abnf = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .use(_name)
    .one_or_more()
    .any_of_chars(" \t")
    .char("=")
    .optional()
    .char("/")
    .one_or_more()
    .any_of_chars(" \t")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an augmented Backus-Naur form grammar: a rule
name followed by a space-delimited ``=`` or ``=/`` definition.
"""
