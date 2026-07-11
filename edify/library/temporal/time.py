"""``time`` — clock-time shape (12h/24h with optional seconds/milliseconds)."""

from __future__ import annotations

from edify import Pattern, any_of

_h24 = (
    Pattern()
    .any_of()
    .subexpression(Pattern().char("2").range("0", "3"))
    .subexpression(Pattern().optional().any_of_chars("01").digit())
    .end()
    .char(":").range("0", "5").digit()
    .optional().group().char(":").range("0", "5").digit()
    .optional().group().char(".").between(1, 6).digit().end()
    .end()
)

_h12 = (
    Pattern()
    .any_of()
    .subexpression(Pattern().char("1").range("0", "2"))
    .subexpression(Pattern().optional().char("0").range("1", "9"))
    .end()
    .char(":").range("0", "5").digit()
    .optional().group().char(":").range("0", "5").digit().end()
    .optional().whitespace_char()
    .any_of_chars("AaPp").any_of_chars("Mm")
)

time = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_h24, _h12))
    .end_of_input()
)
"""Callable :class:`Pattern` for clock-time shapes: 24-hour
``HH:MM[:SS[.ffffff]]`` or 12-hour ``H:MM[:SS] AM/PM``.
"""
