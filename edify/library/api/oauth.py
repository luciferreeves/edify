"""``oauth`` — OAuth 2.0 grant-type value shape."""

from __future__ import annotations

from edify import Pattern

_registered = (
    Pattern()
    .any_of()
    .string("authorization_code")
    .string("client_credentials")
    .string("refresh_token")
    .string("password")
    .string("implicit")
    .string("device_code")
    .end()
)

_extension = (
    Pattern()
    .string("urn:ietf:params:oauth:grant-type:")
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("-_.")
    .end()
)

oauth = Pattern().start_of_input().any_of().use(_extension).use(_registered).end().end_of_input()
"""Callable :class:`Pattern` for an OAuth 2.0 grant type: a registered value or
a ``urn:ietf:params:oauth:grant-type:`` extension URN.
"""
