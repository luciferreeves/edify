"""``semver`` — ``MAJOR.MINOR.PATCH`` SemVer core."""

from __future__ import annotations

from edify import Pattern, any_of


def _core() -> Pattern:
    return any_of(
        Pattern().char("0"),
        Pattern().range("1", "9").zero_or_more().digit(),
    )


semver = Pattern().use(_core()).char(".").use(_core()).char(".").use(_core())
"""Composable :class:`Pattern` fragment for a SemVer ``MAJOR.MINOR.PATCH`` core."""
