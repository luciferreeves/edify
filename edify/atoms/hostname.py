"""``hostname`` — RFC 1123 hostname (dot-separated labels)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.domain_label import domain_label

hostname = Pattern().use(domain_label).zero_or_more().group().char(".").use(domain_label).end()
"""Composable :class:`Pattern` fragment for an RFC 1123 hostname."""
