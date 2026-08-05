"""``cidr`` — IPv4 CIDR notation (``address/prefix``)."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.atoms.ipv4 import ipv4


def _prefix() -> Pattern:
    return any_of(
        Pattern().char("3").range("0", "2"),
        Pattern().range("1", "2").digit(),
        Pattern().digit(),
    )


cidr = Pattern().use(ipv4).char("/").use(_prefix())
"""Composable :class:`Pattern` fragment for IPv4 CIDR notation."""
