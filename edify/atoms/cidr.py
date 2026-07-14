"""``cidr`` — IPv4 CIDR notation (``address/prefix``)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.ipv4 import ipv4

cidr = Pattern().use(ipv4).char("/").between(1, 2).digit()
"""Composable :class:`Pattern` fragment for IPv4 CIDR notation."""
