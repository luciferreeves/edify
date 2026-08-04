"""``keyring`` — armoured OpenPGP key block shape."""

from __future__ import annotations

from edify import Pattern

_label = Pattern().any_of().string("PUBLIC").string("PRIVATE").end().string(" KEY BLOCK")

_body = (
    Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=:").whitespace_char().end()
)

keyring = (
    Pattern()
    .start_of_input()
    .zero_or_more()
    .whitespace_char()
    .string("-----BEGIN PGP ")
    .use(_label)
    .string("-----")
    .use(_body)
    .string("-----END PGP ")
    .use(_label)
    .string("-----")
    .zero_or_more()
    .whitespace_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for an armoured OpenPGP key block: a ``PUBLIC KEY
BLOCK`` or ``PRIVATE KEY BLOCK``.
"""
