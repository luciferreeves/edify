"""``isodatetime`` — ISO 8601 combined date-time shape."""

from __future__ import annotations

from edify import Pattern

isodatetime = (
    Pattern()
    .exactly(4)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .any_of_chars("Tt ")
    .exactly(2)
    .digit()
    .char(":")
    .exactly(2)
    .digit()
    .optional()
    .group()
    .char(":")
    .exactly(2)
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .end()
    .optional()
    .group()
    .any_of()
    .any_of_chars("Zz")
    .subexpression(
        Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit()
    )
    .end()
    .end()
)
"""Composable :class:`Pattern` fragment for an ISO 8601 combined date-time."""
