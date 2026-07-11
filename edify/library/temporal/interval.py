"""``interval`` — ISO 8601 time-interval shape (``start/end`` or ``start/duration``)."""

from __future__ import annotations

from edify import Pattern, any_of


def _iso_extended() -> Pattern:
    return (
        Pattern()
        .exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
        .any_of_chars("Tt ")
        .exactly(2).digit().char(":").exactly(2).digit()
        .optional().group().char(":").exactly(2).digit()
        .optional().group().char(".").one_or_more().digit().end()
        .end()
        .optional().group().any_of()
        .any_of_chars("Zz")
        .subexpression(
            Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit()
        )
        .end().end()
    )


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


interval = (
    Pattern()
    .start_of_input()
    .subexpression(_iso_extended())
    .char("/")
    .subexpression(any_of(_iso_extended(), _duration_body()))
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 8601 time-interval shape:
``start-datetime/end-datetime`` or ``start-datetime/duration``.
"""
