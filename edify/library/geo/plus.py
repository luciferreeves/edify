"""``plus`` — Google Plus Code (Open Location Code) shape."""

from __future__ import annotations

from edify import Pattern

_PLUS_CODE_ALPHABET = "23456789CFGHJMPQRVWX"

plus = (
    Pattern()
    .start_of_input()
    .between(2, 8)
    .any_of_chars(_PLUS_CODE_ALPHABET)
    .char("+")
    .between(2, 3)
    .any_of_chars(_PLUS_CODE_ALPHABET)
    .optional()
    .group()
    .one_or_more()
    .whitespace_char()
    .one_or_more()
    .any_char()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a Google Plus Code (Open Location Code)."""

del _PLUS_CODE_ALPHABET
