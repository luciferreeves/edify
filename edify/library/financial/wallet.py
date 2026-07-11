"""``wallet`` — cryptocurrency wallet-address shape (base58 or hex)."""

from __future__ import annotations

from edify import Pattern, any_of

_bitcoin_legacy = (
    Pattern()
    .any_of_chars("13")
    .between(25, 34)
    .any_of()
    .range("a", "k")
    .range("m", "z")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("1", "9")
    .end()
)

_bitcoin_bech32 = (
    Pattern().string("bc1").between(25, 89).any_of().range("a", "z").range("0", "9").end()
)

_ethereum = (
    Pattern()
    .string("0x")
    .exactly(40)
    .any_of()
    .range("a", "f")
    .range("A", "F")
    .range("0", "9")
    .end()
)

_litecoin = (
    Pattern()
    .any_of_chars("LM3")
    .between(26, 33)
    .any_of()
    .range("a", "k")
    .range("m", "z")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("1", "9")
    .end()
)

_dogecoin = (
    Pattern()
    .char("D")
    .any_of()
    .range("5", "9")
    .range("A", "H")
    .range("J", "N")
    .range("P", "U")
    .end()
    .exactly(32)
    .any_of()
    .range("1", "9")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("a", "k")
    .range("m", "z")
    .end()
)

_dash = (
    Pattern()
    .char("X")
    .exactly(33)
    .any_of()
    .range("1", "9")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("a", "k")
    .range("m", "z")
    .end()
)

wallet = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_bitcoin_legacy, _bitcoin_bech32, _ethereum, _litecoin, _dogecoin, _dash))
    .end_of_input()
)
"""Callable :class:`Pattern` for cryptocurrency-wallet address shapes:
Bitcoin (legacy, SegWit, Bech32), Ethereum, Litecoin, Dogecoin, Dash.
"""

del _bitcoin_legacy, _bitcoin_bech32, _ethereum, _litecoin, _dogecoin, _dash
