"""``sitemap`` — XML sitemap document shape."""

from __future__ import annotations

from edify import Pattern

_declaration = Pattern().string("<?xml").zero_or_more().any_char()

sitemap = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .optional()
    .use(_declaration)
    .char("<")
    .any_of()
    .string("urlset")
    .string("sitemapindex")
    .end()
    .zero_or_more()
    .any_char()
    .string("http://www.sitemaps.org/schemas/sitemap/")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an XML sitemap: a ``<urlset`` or
``<sitemapindex`` root carrying the sitemap schema namespace.
"""
