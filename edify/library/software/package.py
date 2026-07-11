"""``package`` — npm/pypi-style package identifier shape."""

from __future__ import annotations

from edify import Pattern

package = (
    Pattern()
    .start_of_input()
    .optional()
    .group()
    .char("@")
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .end()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .char("-")
    .end()
    .char("/")
    .end()
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .end()
    .between(0, 213)
    .any_of()
    .range("a", "z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an npm/pypi-style package identifier."""
