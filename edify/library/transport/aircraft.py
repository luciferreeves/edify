"""``aircraft`` — aircraft-registration shape (e.g. ``N123AB``, ``G-ABCD``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

aircraft = RegexBackedPattern(r"^[A-Z]{1,2}-?[A-Z0-9]{1,5}$")
"""Callable :class:`Pattern` for an aircraft-registration mark."""
