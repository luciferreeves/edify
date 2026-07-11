"""``printable`` — printable-character string shape."""

from __future__ import annotations

from edify import Pattern


def _not_ctrl() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .range("\x00", "\x1F")
        .char("\x7F")
        .end()
        .end()
        .any_char()
    )


printable = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .subexpression(_not_ctrl())
    .end_of_input()
)
"""Callable :class:`Pattern` for a printable-character string
(anything except ASCII control codes ``0x00``-``0x1F`` and ``0x7F``).
"""
