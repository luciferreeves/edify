"""``ipv6`` — permissive IPv6 address (full, abbreviated, or ``::``)."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.atoms.nibble import nibble

ipv6 = any_of(
    Pattern()
    .exactly(7)
    .group()
    .between(1, 4)
    .use(nibble)
    .char(":")
    .end()
    .between(1, 4)
    .use(nibble),
    Pattern().between(1, 7).group().between(1, 4).use(nibble).char(":").end().char(":"),
    Pattern().string("::"),
)
"""Composable :class:`Pattern` fragment for a permissive IPv6 address."""
