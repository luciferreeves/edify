"""``wallet`` — cryptocurrency wallet-address shape (base58 or hex)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

wallet = RegexBackedPattern(
    r"^(?:"
    r"[13][a-km-zA-HJ-NP-Z1-9]{25,34}"
    r"|bc1[a-z0-9]{25,89}"
    r"|0x[a-fA-F0-9]{40}"
    r"|[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}"
    r"|D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}"
    r"|X[1-9A-HJ-NP-Za-km-z]{33}"
    r")$"
)
"""Callable :class:`Pattern` for cryptocurrency-wallet address shapes:
Bitcoin (legacy, SegWit, Bech32), Ethereum, Litecoin, Dogecoin, Dash.
"""
