"""``coordinate`` — latitude/longitude coordinate shape."""

from __future__ import annotations

from edify import Pattern, any_of

_lat_ninety = (
    Pattern()
    .string("90")
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .char("0")
    .end()
)

_lat_below_ninety = (
    Pattern()
    .optional()
    .range("0", "8")
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
)

_lon_one_eighty = (
    Pattern()
    .string("180")
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .char("0")
    .end()
)

_lon_below_one_eighty_integer = any_of(
    Pattern().char("1").range("0", "7").digit(),
    Pattern().optional().range("0", "9").digit(),
)

_lon_below_one_eighty = (
    Pattern()
    .subexpression(_lon_below_one_eighty_integer)
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
)

coordinate = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .subexpression(any_of(_lat_ninety, _lat_below_ninety))
    .zero_or_more()
    .whitespace_char()
    .char(",")
    .zero_or_more()
    .whitespace_char()
    .optional()
    .char("-")
    .subexpression(any_of(_lon_one_eighty, _lon_below_one_eighty))
    .end_of_input()
)
"""Callable :class:`Pattern` for the ``latitude,longitude`` coordinate shape."""

del (
    _lat_ninety,
    _lat_below_ninety,
    _lon_one_eighty,
    _lon_below_one_eighty_integer,
    _lon_below_one_eighty,
)
