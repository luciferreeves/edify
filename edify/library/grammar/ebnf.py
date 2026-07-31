"""``ebnf`` — extended Backus-Naur form grammar shape."""

from __future__ import annotations

from edify import Pattern

_name = Pattern().letter().zero_or_more().any_of().alphanumeric().any_of_chars("_- ").end()

ebnf = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .use(_name)
    .char("=")
    .zero_or_more()
    .any_char()
    .char(";")
    .zero_or_more()
    .whitespace_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an extended Backus-Naur form grammar: a bare
rule name, ``=``, and a ``;``-terminated definition.
"""
