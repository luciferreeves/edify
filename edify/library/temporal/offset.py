"""``offset`` — UTC offset shape (``±HH:MM`` or ``Z``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

offset = RegexBackedPattern(r"^(?:Z|[+-](?:0\d|1[0-4]):?[0-5]\d)$")
"""Callable :class:`Pattern` for the UTC-offset shape: ``Z`` for UTC or
``±HH:MM`` / ``±HHMM`` with range ``-14:00`` to ``+14:00``.
"""
