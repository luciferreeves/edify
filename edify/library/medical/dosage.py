"""``dosage`` — pharmaceutical dosage shape (``10mg``, ``5.5 ml/kg``)."""

from __future__ import annotations

from edify import Pattern


def _unit() -> Pattern:
    return (
        Pattern()
        .any_of()
        .string("mg")
        .char("g")
        .string("kg")
        .string("ml")
        .char("l")
        .string("mcg")
        .string("iu")
        .end()
    )


dosage = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .whitespace_char()
    .subexpression(_unit())
    .optional()
    .group()
    .char("/")
    .any_of()
    .string("kg")
    .string("day")
    .string("dose")
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a pharmaceutical dosage shape:
digits with optional decimal + unit (``mg``/``g``/``kg``/``ml``/``l``/``mcg``/``iu``)
and optional per-``kg``/``day``/``dose`` qualifier.
"""
