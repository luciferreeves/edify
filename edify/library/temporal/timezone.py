"""``timezone`` — IANA / abbreviation timezone shape."""

from __future__ import annotations

from edify import Pattern, any_of

_iana_seg = (
    Pattern()
    .uppercase()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .char("_")
    .char("+")
    .char("-")
    .end()
)
_iana = (
    Pattern()
    .subexpression(_iana_seg)
    .one_or_more()
    .group()
    .char("/")
    .subexpression(_iana_seg)
    .end()
)
_short = any_of(
    Pattern().string("UTC"),
    Pattern().string("GMT"),
    Pattern().string("UT"),
    Pattern().string("Z"),
)
_abbrev = Pattern().between(2, 5).uppercase()

timezone = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_iana, _short, _abbrev))
    .end_of_input()
)
"""Callable :class:`Pattern` for the timezone shape:
IANA region/city (``America/Los_Angeles``), or short abbreviation
(``UTC``, ``PST``, ``EST``, …).
"""
