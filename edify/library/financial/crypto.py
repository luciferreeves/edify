"""``crypto`` — cryptocurrency ticker/mint identifier shape."""

from __future__ import annotations

from edify import Pattern

crypto = (
    Pattern()
    .start_of_input()
    .between(3, 10)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a cryptocurrency ticker shape:
3-10 uppercase-alphanumeric characters (``BTC``, ``ETH``, ``USDT``, ``SHIB``, …).
"""
