"""``bump`` — semver bump keyword shape."""

from __future__ import annotations

from edify import Pattern

bump = (
    Pattern()
    .start_of_input()
    .any_of()
    .string("major")
    .string("minor")
    .string("patch")
    .string("premajor")
    .string("preminor")
    .string("prepatch")
    .string("prerelease")
    .string("release")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a semver bump keyword."""
