"""``label`` — one RFC 1123 DNS label."""

from __future__ import annotations

from edify import Pattern

label = (
    Pattern()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .optional()
    .group()
    .between(0, 61)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end()
)
"""Composable :class:`Pattern` fragment for one RFC 1123 DNS label
(letter/digit start, up to 63 chars, letter/digit end).
"""
