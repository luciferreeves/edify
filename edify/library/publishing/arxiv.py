"""``arxiv`` — arXiv identifier shape (new format ``YYMM.NNNNN`` or legacy ``category/YYMMNNN``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

arxiv = RegexBackedPattern(
    r"^(?:\d{4}\.\d{4,5}(?:v\d+)?|[a-z]{2,10}(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)$"
)
"""Callable :class:`Pattern` for an arXiv identifier."""
