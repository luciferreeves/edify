"""``ipv6`` — IPv6 address in full or ``::``-compressed form."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.atoms.nibble import nibble


def _hex_group() -> Pattern:
    return Pattern().between(1, 4).use(nibble)


def _leading(groups: int) -> Pattern:
    if groups == 1:
        return _hex_group().char(":")
    return Pattern().between(1, groups).group().use(_hex_group()).char(":").end()


def _trailing(groups: int) -> Pattern:
    if groups == 1:
        return Pattern().char(":").use(_hex_group())
    return Pattern().between(1, groups).group().char(":").use(_hex_group()).end()


def _full() -> Pattern:
    return Pattern().exactly(7).group().use(_hex_group()).char(":").end().use(_hex_group())


def _compressed(leading_groups: int, trailing_groups: int) -> Pattern:
    return _leading(leading_groups).use(_trailing(trailing_groups))


def _compressed_tail() -> Pattern:
    return _leading(7).char(":")


def _compressed_head() -> Pattern:
    return Pattern().char(":").group().any_of().use(_trailing(7)).char(":").end().end()


ipv6 = any_of(
    _full(),
    _compressed_tail(),
    _compressed(6, 1),
    _compressed(5, 2),
    _compressed(4, 3),
    _compressed(3, 4),
    _compressed(2, 5),
    _compressed(1, 6),
    _compressed_head(),
)
"""Composable :class:`Pattern` fragment for an IPv6 address."""
