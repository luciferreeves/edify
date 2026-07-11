"""``phone`` — permissive international or short-code phone-number shape."""

from __future__ import annotations

from edify import Pattern, any_of

_international = (
    Pattern()
    .optional()
    .char("+")
    .between_lazy(1, 4)
    .digit()
    .optional()
    .any_of()
    .char("-")
    .char(".")
    .whitespace_char()
    .end()
    .optional()
    .char("(")
    .between_lazy(1, 3)
    .digit()
    .optional()
    .char(")")
    .optional()
    .any_of()
    .char("-")
    .char(".")
    .whitespace_char()
    .end()
    .between(1, 4)
    .digit()
    .optional()
    .any_of()
    .char("-")
    .char(".")
    .whitespace_char()
    .end()
    .between(1, 4)
    .digit()
    .optional()
    .any_of()
    .char("-")
    .char(".")
    .whitespace_char()
    .end()
    .between(1, 9)
    .digit()
)
_short = Pattern().between(2, 4).digit()

phone = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_international, _short))
    .end_of_input()
)
"""Callable :class:`Pattern` for phone-number shapes: permissive international
form (optional ``+``, country code, area code, and dash/dot/space separators)
or 2-4 digit short-code fallback.
"""
