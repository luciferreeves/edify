"""``cron`` — cron-expression shape (5 or 6 whitespace-separated fields)."""

from __future__ import annotations

from edify import Pattern, any_of

_alias = (
    Pattern()
    .char("@")
    .group()
    .any_of()
    .string("annually")
    .string("yearly")
    .string("monthly")
    .string("weekly")
    .string("daily")
    .string("hourly")
    .string("reboot")
    .end()
    .end()
)
_field = (
    Pattern()
    .one_or_more()
    .any_of()
    .char("*")
    .char("?")
    .range("0", "9")
    .char("/")
    .char(",")
    .char("-")
    .end()
)
_expr = (
    Pattern()
    .between(4, 5)
    .group()
    .subexpression(_field)
    .one_or_more()
    .whitespace_char()
    .end()
    .subexpression(_field)
)

cron = Pattern().start_of_input().subexpression(any_of(_alias, _expr)).end_of_input()
"""Callable :class:`Pattern` for cron-expression shapes: shortcut aliases
(``@daily`` etc.) or 5-/6-field whitespace-separated expressions.
"""
