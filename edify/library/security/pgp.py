"""``pgp`` — armoured OpenPGP block shape."""

from __future__ import annotations

from edify import Pattern

_label = Pattern().uppercase().zero_or_more().any_of().uppercase().digit().any_of_chars(" ").end()

_body = (
    Pattern().zero_or_more().any_of().alphanumeric().any_of_chars("+/=:").whitespace_char().end()
)

pgp = (
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
"""Callable :class:`Pattern` for an armoured OpenPGP block: a message,
signature, or key block between ``-----BEGIN PGP …-----`` markers.
"""
