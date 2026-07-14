"""``money`` — currency code combined with an amount (either order)."""

from __future__ import annotations

from edify import Pattern, any_of

_amount = Pattern().one_or_more().digit().optional().group().char(".").one_or_more().digit().end()

money = any_of(
    Pattern().exactly(3).uppercase().optional().whitespace_char().use(_amount),
    Pattern().use(_amount).optional().whitespace_char().exactly(3).uppercase(),
)
"""Composable :class:`Pattern` fragment for a currency + amount value."""
