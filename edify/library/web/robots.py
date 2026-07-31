"""``robots`` — robots exclusion file shape."""

from __future__ import annotations

from edify import Pattern

_directive = (
    Pattern()
    .any_of()
    .string("user-agent")
    .string("disallow")
    .string("allow")
    .string("sitemap")
    .string("crawl-delay")
    .string("host")
    .end()
    .zero_or_more()
    .whitespace_char()
    .char(":")
)

_comment = Pattern().char("#")

robots = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .any_of()
    .use(_comment)
    .use(_directive)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
    .ignore_case()
)
"""Callable :class:`Pattern` for a robots exclusion file: a comment or a
``User-agent``/``Disallow``/``Allow``/``Sitemap`` directive.
"""
