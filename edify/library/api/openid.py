"""``openid`` — OpenID Connect discovery endpoint shape."""

from __future__ import annotations

from edify import Pattern

_host = (
    Pattern()
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("-.")
    .end()
    .optional()
    .group()
    .char(":")
    .between(1, 5)
    .digit()
    .end()
)

_path = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("-._~/").end()

openid = (
    Pattern()
    .start_of_input()
    .optional()
    .group()
    .string("https://")
    .use(_host)
    .end()
    .use(_path)
    .string("/.well-known/openid-configuration")
    .optional()
    .char("/")
    .end_of_input()
)
"""Callable :class:`Pattern` for an OpenID Connect discovery endpoint: a
``/.well-known/openid-configuration`` path, with or without an ``https`` origin.
"""
