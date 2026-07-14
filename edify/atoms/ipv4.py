"""``ipv4`` — dotted-quad IPv4 address."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.octet import octet

ipv4 = Pattern().use(octet).exactly(3).group().char(".").use(octet).end()
"""Composable :class:`Pattern` fragment for a dotted-quad IPv4 address."""
