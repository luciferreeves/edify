"""``did`` — W3C Decentralized Identifier ``did:METHOD:IDENTIFIER``."""

from __future__ import annotations

from edify import Pattern

did = (
    Pattern()
    .start_of_input()
    .string("did:")
    .one_or_more().any_of().range("a", "z").range("0", "9").end()
    .char(":")
    .one_or_more().any_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for the DID shape: literal ``did:`` +
lowercase-alphanumeric method name + colon + identifier body.
"""
