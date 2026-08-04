"""``ssh`` — SSH key shape."""

from __future__ import annotations

from edify import Pattern

_key_type = (
    Pattern()
    .any_of()
    .string("ssh-rsa")
    .string("ssh-dss")
    .string("ssh-ed25519")
    .string("sk-ssh-ed25519@openssh.com")
    .subexpression(Pattern().string("ecdsa-sha2-nistp").exactly(3).digit())
    .end()
)

_public = (
    Pattern()
    .use(_key_type)
    .one_or_more()
    .whitespace_char()
    .one_or_more()
    .any_of()
    .alphanumeric()
    .any_of_chars("+/=")
    .end()
    .zero_or_more()
    .any_char()
)

_body = Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=").whitespace_char().end()

_private = (
    Pattern()
    .string("-----BEGIN OPENSSH PRIVATE KEY-----")
    .use(_body)
    .string("-----END OPENSSH PRIVATE KEY-----")
    .zero_or_more()
    .whitespace_char()
)

ssh = Pattern().start_of_input().any_of().use(_private).use(_public).end().end_of_input().dot_all()
"""Callable :class:`Pattern` for an SSH key: an ``ssh-rsa``/``ssh-ed25519``
style public-key line, or an OpenSSH private-key block.
"""
