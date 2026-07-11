"""``arn`` — Amazon Resource Name (``arn:partition:service:region:account:resource``)."""

from __future__ import annotations

from edify import Pattern

arn = (
    Pattern()
    .start_of_input()
    .string("arn:")
    .one_or_more().any_of().range("a", "z").char("-").end()
    .char(":")
    .one_or_more().any_of().range("a", "z").range("0", "9").char("-").end()
    .char(":")
    .zero_or_more().any_of().range("a", "z").range("0", "9").char("-").end()
    .char(":")
    .zero_or_more().digit()
    .char(":")
    .one_or_more().any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for the AWS ARN shape:
``arn:PARTITION:SERVICE:REGION:ACCOUNT_ID:RESOURCE``.
"""
