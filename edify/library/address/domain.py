"""``domain`` — DNS domain name shape (label.label.tld)."""

from __future__ import annotations

from edify import Pattern

domain = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .group()
    .alphanumeric()
    .optional()
    .group()
    .at_most(61)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .alphanumeric()
    .end()
    .char(".")
    .end()
    .between(2, 63)
    .letter()
    .end_of_input()
)
"""Callable :class:`Pattern` for the DNS domain name shape:
at least one label followed by a TLD of 2-63 letters.
"""
