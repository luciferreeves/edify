"""``hostname`` — RFC 1123 hostname (dot-separated labels)."""

from __future__ import annotations

from edify import Pattern
from edify.atoms.label import label

hostname = Pattern().use(label).zero_or_more().group().char(".").use(label).end()
"""Composable :class:`Pattern` fragment for an RFC 1123 hostname."""
