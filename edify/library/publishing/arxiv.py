"""``arxiv`` — arXiv identifier shape (new format ``YYMM.NNNNN`` or legacy ``category/YYMMNNN``)."""

from __future__ import annotations

from edify import Pattern, any_of

_new = (
    Pattern()
    .exactly(4)
    .digit()
    .char(".")
    .between(4, 5)
    .digit()
    .optional()
    .group()
    .char("v")
    .one_or_more()
    .digit()
    .end()
)
_old = (
    Pattern()
    .between(2, 10)
    .lowercase()
    .optional()
    .group()
    .char(".")
    .exactly(2)
    .uppercase()
    .end()
    .char("/")
    .exactly(7)
    .digit()
    .optional()
    .group()
    .char("v")
    .one_or_more()
    .digit()
    .end()
)

arxiv = Pattern().start_of_input().subexpression(any_of(_new, _old)).end_of_input()
"""Callable :class:`Pattern` for an arXiv identifier."""
