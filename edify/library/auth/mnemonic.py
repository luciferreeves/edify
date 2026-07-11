"""``mnemonic`` — BIP-39 mnemonic phrase shape."""

from __future__ import annotations

from edify import Pattern

mnemonic = (
    Pattern()
    .start_of_input()
    .between(11, 23)
    .group()
    .one_or_more()
    .lowercase()
    .char(" ")
    .end()
    .one_or_more()
    .lowercase()
    .end_of_input()
)
"""Callable :class:`Pattern` for a BIP-39 mnemonic phrase: 12 to 24
lowercase words separated by single spaces.
"""
