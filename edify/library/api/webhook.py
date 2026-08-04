"""``webhook`` — webhook callback endpoint shape."""

from __future__ import annotations

from edify import Pattern

_host = (
    Pattern()
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("-")
    .end()
    .one_or_more()
    .group()
    .char(".")
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("-")
    .end()
    .end()
)

_port = Pattern().char(":").between(1, 5).digit()

_tail = (
    Pattern().char("/").zero_or_more().any_of().alphanumeric().any_of_chars("-._~/%?&=+:@#").end()
)

webhook = (
    Pattern()
    .start_of_input()
    .string("https://")
    .use(_host)
    .optional()
    .use(_port)
    .use(_tail)
    .end_of_input()
)
"""Callable :class:`Pattern` for a webhook callback endpoint: an ``https`` URL
with a dotted host and a delivery path.
"""
