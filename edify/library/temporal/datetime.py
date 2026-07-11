"""``datetime`` — combined date-time shape (ISO 8601 / RFC 3339 / common variants)."""

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


def _iso_basic() -> Pattern:
    return (
        Pattern()
        .exactly(4).digit().exactly(2).digit().exactly(2).digit()
        .any_of_chars("Tt")
        .exactly(2).digit().exactly(2).digit().exactly(2).digit()
        .optional().group().any_of()
        .any_of_chars("Zz")
        .subexpression(Pattern().any_of_chars("+-").exactly(4).digit())
        .end().end()
    )


datetime = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_iso_extended(), _iso_basic()))
    .end_of_input()
)
"""Callable :class:`Pattern` for combined date-time shapes: ISO 8601 /
RFC 3339 forms with ``T`` or space separator, optional fractional seconds,
optional timezone suffix.
"""
