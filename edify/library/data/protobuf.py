"""``protobuf`` — protocol-buffer schema source shape."""

from __future__ import annotations

from edify import Pattern

_syntax = (
    Pattern()
    .string("syntax")
    .zero_or_more()
    .whitespace_char()
    .char("=")
    .zero_or_more()
    .whitespace_char()
    .any_of_chars("\"'")
    .string("proto")
    .digit()
)

_declaration = (
    Pattern()
    .any_of()
    .string("package")
    .string("import")
    .string("message")
    .string("service")
    .string("enum")
    .end()
    .one_or_more()
    .whitespace_char()
)

_comment = Pattern().string("//")

protobuf = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_syntax)
    .use(_comment)
    .use(_declaration)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a protocol-buffer schema: a ``syntax``
declaration, a comment, or a ``package``/``import``/``message``/``service``/
``enum`` keyword.
"""
