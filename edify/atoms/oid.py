"""``oid`` — dotted numeric object identifier."""

from __future__ import annotations

from edify import Pattern

oid = Pattern().one_or_more().digit().one_or_more().group().char(".").one_or_more().digit().end()
"""Composable :class:`Pattern` fragment for a dotted numeric OID."""
