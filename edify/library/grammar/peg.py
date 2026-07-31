"""``peg`` — parsing expression grammar shape."""

from __future__ import annotations

from edify import Pattern

_name = Pattern().letter().zero_or_more().any_of().alphanumeric().char("_").end()

peg = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .use(_name)
    .zero_or_more()
    .any_of_chars(" \t")
    .string("<-")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a parsing expression grammar: a rule name
followed by the ``<-`` arrow.
"""
