"""``favicon`` — favicon file name or URL path shape."""

from __future__ import annotations

from edify import Pattern


def _not_ctrl_or_seps() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .range("\x00", "\x1f")
        .char("/")
        .char("\\")
        .end()
        .end()
        .any_char()
    )


favicon = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .group()
    .one_or_more()
    .subexpression(_not_ctrl_or_seps())
    .char("/")
    .end()
    .string("favicon")
    .char(".")
    .group()
    .any_of()
    .string("ico")
    .string("png")
    .string("svg")
    .string("gif")
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a favicon file name or URL path."""
