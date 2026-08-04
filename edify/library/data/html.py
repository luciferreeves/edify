"""``html`` — HTML document shape."""

from __future__ import annotations

from edify import Pattern

_doctype = Pattern().string("<!doctype").one_or_more().whitespace_char()

_root = Pattern().string("<html")

_comment = Pattern().string("<!--")

html = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_doctype)
    .use(_comment)
    .use(_root)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
    .ignore_case()
)
"""Callable :class:`Pattern` for an HTML document: a ``<!DOCTYPE`` declaration, a
leading comment, or an ``<html`` root element.
"""
