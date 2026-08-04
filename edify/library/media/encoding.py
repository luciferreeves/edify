"""``encoding`` — HTTP content-coding token shape."""

from __future__ import annotations

from edify import Pattern

_token = (
    Pattern()
    .any_of()
    .string("gzip")
    .string("compress")
    .string("deflate")
    .string("br")
    .string("zstd")
    .string("identity")
    .string("x-gzip")
    .string("x-compress")
    .char("*")
    .end()
)

_quality = (
    Pattern()
    .zero_or_more()
    .whitespace_char()
    .string(";q=")
    .digit()
    .optional()
    .group()
    .char(".")
    .between(1, 3)
    .digit()
    .end()
)

encoding = Pattern().start_of_input().use(_token).optional().use(_quality).end_of_input()
"""Callable :class:`Pattern` for an HTTP content-coding token such as ``gzip``
or ``br``, with an optional ``;q=`` quality value.
"""
