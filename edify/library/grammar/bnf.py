"""``bnf`` — Backus-Naur form grammar shape."""

from __future__ import annotations

from edify import Pattern

_name = Pattern().char("<").one_or_more().anything_but_chars("<>\r\n").char(">")

bnf = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .use(_name)
    .zero_or_more()
    .whitespace_char()
    .string("::=")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a Backus-Naur form grammar: an
``<angle-bracketed>`` rule name followed by ``::=``.
"""
