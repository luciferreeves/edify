"""``mac`` — IEEE 802 MAC-address 6-octet hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import RegexBuilder
from edify.library._support.coerce import as_pattern


def _build() -> object:
    chain = (
        RegexBuilder()
        .start_of_input()
        .exactly(5)
        .group()
        .exactly(2).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .any_of_chars(":-")
        .end()
        .exactly(2).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .end_of_input()
    )
    return as_pattern(chain)


mac = _build()
"""Callable :class:`Pattern` that validates the IEEE 802 MAC-address form:
six ``:``- or ``-``-separated hex octets (either case).
"""

del _build
