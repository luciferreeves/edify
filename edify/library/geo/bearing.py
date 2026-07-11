"""``bearing`` — compass-bearing shape (0-360 degrees)."""

from __future__ import annotations

from edify import Pattern

bearing = (
    Pattern()
    .start_of_input()
    .any_of()
    .subexpression(
        Pattern().string("360").optional().group().char(".").one_or_more().char("0").end()
    )
    .subexpression(
        Pattern()
        .any_of()
        .subexpression(Pattern().char("3").range("0", "5").digit())
        .subexpression(Pattern().range("1", "2").digit().digit())
        .subexpression(Pattern().between(1, 2).digit())
        .end()
        .optional()
        .group()
        .char(".")
        .one_or_more()
        .digit()
        .end()
    )
    .end()
    .optional()
    .char("°")
    .end_of_input()
)
"""Callable :class:`Pattern` for a compass bearing (0-360 degrees)."""
