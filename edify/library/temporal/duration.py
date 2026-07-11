"""``duration`` — ISO 8601 duration shape (``PnYnMnDTnHnMnS``)."""

from __future__ import annotations

from edify import Pattern


def _num_with_letter(letter: str) -> Pattern:
    return (
        Pattern()
        .optional()
        .group()
        .one_or_more().digit()
        .optional().group().char(".").one_or_more().digit().end()
        .char(letter)
        .end()
    )


def _duration_body() -> Pattern:
    return (
        Pattern()
        .char("P")
        .assert_ahead().any_char().end()
        .subexpression(_num_with_letter("Y"))
        .subexpression(_num_with_letter("M"))
        .subexpression(_num_with_letter("W"))
        .subexpression(_num_with_letter("D"))
        .optional().group()
        .char("T").assert_ahead().digit().end()
        .subexpression(_num_with_letter("H"))
        .subexpression(_num_with_letter("M"))
        .subexpression(_num_with_letter("S"))
        .end()
    )


duration = (
    Pattern()
    .start_of_input()
    .subexpression(_duration_body())
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 8601 duration shape:
``PnYnMnDTnHnMnS`` with optional fractional components.
"""
