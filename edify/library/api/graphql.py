"""``graphql`` — GraphQL document shape."""

from __future__ import annotations

from edify import Pattern

_keyword = (
    Pattern()
    .any_of()
    .string("query")
    .string("mutation")
    .string("subscription")
    .string("fragment")
    .string("schema")
    .string("type")
    .string("input")
    .string("interface")
    .string("union")
    .string("enum")
    .string("scalar")
    .string("directive")
    .string("extend")
    .end()
    .any_of()
    .whitespace_char()
    .any_of_chars("{(@")
    .end()
)

_anonymous = (
    Pattern()
    .char("{")
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .letter()
    .any_of_chars("_.")
    .end()
    .zero_or_more()
    .any_char()
    .char("}")
)

_comment = Pattern().char("#")

graphql = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_keyword)
    .use(_comment)
    .use(_anonymous)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a GraphQL document: an operation, fragment, or
type-system definition keyword, a comment, or an anonymous selection set.
"""
