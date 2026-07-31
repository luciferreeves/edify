"""``age`` — age recipient or identity shape."""

from __future__ import annotations

from edify import Pattern

_bech32 = Pattern().any_of().range("0", "9").range("a", "z").end()

_recipient = Pattern().string("age1").between(8, 128).use(_bech32)

_identity = (
    Pattern()
    .string("AGE-SECRET-KEY-1")
    .between(8, 128)
    .any_of()
    .range("0", "9")
    .range("A", "Z")
    .end()
)

age = Pattern().start_of_input().any_of().use(_identity).use(_recipient).end().end_of_input()
"""Callable :class:`Pattern` for an age key: an ``age1…`` recipient or an
``AGE-SECRET-KEY-1…`` identity.
"""
