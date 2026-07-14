"""``bic`` — Bank Identifier Code / SWIFT code shape."""

from __future__ import annotations

from edify import Pattern

bic = (
    Pattern()
    .exactly(4)
    .uppercase()
    .exactly(2)
    .uppercase()
    .exactly(2)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .optional()
    .group()
    .exactly(3)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end()
)
"""Composable :class:`Pattern` fragment for a BIC/SWIFT code."""
