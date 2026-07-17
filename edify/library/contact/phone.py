"""``phone`` — multi-locale phone shapes: international/national display and service codes."""

from __future__ import annotations

from edify import Pattern, any_of

_separator = Pattern().optional().any_of_chars(" .-")

_plain_group = Pattern().between(1, 4).digit()
_parenthesised_group = Pattern().char("(").between(1, 4).digit().char(")")
_group = any_of(_plain_group, _parenthesised_group)

_international_prefix = (
    Pattern()
    .optional()
    .group()
    .any_of()
    .char("+")
    .string("00")
    .end()
    .optional()
    .any_of_chars(" .-")
    .end()
)

_number = (
    Pattern()
    .subexpression(_international_prefix)
    .subexpression(_group)
    .between(1, 7)
    .group()
    .subexpression(_separator)
    .subexpression(_group)
    .end()
)

_service = Pattern().between(2, 6).digit()

phone = Pattern().start_of_input().subexpression(any_of(_number, _service)).end_of_input()
"""Callable :class:`Pattern` for multi-locale phone-number display shapes.

Guarantees:
    * International form: an optional ``+`` or ``00`` prefix, then two to eight
      digit groups of one to four digits each, separated by an optional single
      space, dot, or dash.
    * Any single group may be parenthesised, covering leading and inline area
      codes such as ``(555) 123-4567`` and ``+44 (0)20 7946 0958``.
    * Variable national grouping — three-group North American, five-group French,
      and every shape in between are accepted.
    * Service and short codes of two to six digits, covering emergency and
      abbreviated-dialling numbers.
    * Anchored at both ends.

Does not guarantee:
    * ITU E.164 canonical form or per-country structural validity — the pattern
      accepts the permissive display forms real inputs use, not a single locale's
      exact digit count.
    * Separator discipline beyond a single character between groups — doubled
      separators such as ``555--123--4567`` are rejected.
    * Letters or vanity spellings — only digits, separators, and parentheses match.
"""
