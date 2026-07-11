"""``mnemonic`` — BIP-39 mnemonic phrase shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

mnemonic = RegexBackedPattern(r"^(?:[a-z]+ ){11,23}[a-z]+$")
"""Callable :class:`Pattern` for a BIP-39 mnemonic phrase: 12 to 24
lowercase words separated by single spaces.
"""
