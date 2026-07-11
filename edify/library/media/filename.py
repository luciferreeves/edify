"""``filename`` — valid filename with extension shape."""

from __future__ import annotations

from edify import Pattern


def _not_ctrl_or_reserved() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .range("\x00", "\x1f")
        .char("/")
        .char("\\")
        .char(":")
        .char("*")
        .char("?")
        .char('"')
        .char("<")
        .char(">")
        .char("|")
        .end()
        .end()
        .any_char()
    )


filename = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .subexpression(_not_ctrl_or_reserved())
    .char(".")
    .between(1, 10)
    .alphanumeric()
    .end_of_input()
)
"""Callable :class:`Pattern` for a valid file name with extension."""
