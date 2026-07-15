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

phone = Pattern().start_of_input().subexpression(any_of(_international, _short)).end_of_input()
"""Callable :class:`Pattern` for permissive international or 2-4 digit short-code phone shapes.

Guarantees:
    * International form: optional ``+``, 1-4 country-code digits, optional
      parenthesised area code, and dash/dot/space separators.
    * Short-code fallback for 2-4 digit service numbers.
    * Anchored at both ends.

Does not guarantee:
    * ITU E.164 canonical form — the pattern is deliberately permissive to
      accept the display forms real inputs use.
    * Per-country structural validity — full locale coverage lands with the
      dedicated locale-expansion work.
    * Missed shapes (parenthesised area codes with mixed separators, 4-digit-only
      service numbers outside the short-code range) — expect false rejects for
      unusual inputs.
"""
