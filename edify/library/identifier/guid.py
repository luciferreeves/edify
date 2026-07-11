"""``guid`` — Microsoft-flavour GUID 8-4-4-4-12 hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import RegexBuilder
from edify.library._support.coerce import as_pattern


def _build() -> object:
    chain = (
        RegexBuilder()
        .start_of_input()
        .optional().char("{")
        .exactly(8).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .char("-")
        .exactly(4).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .char("-")
        .exactly(4).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .char("-")
        .exactly(4).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .char("-")
        .exactly(12).any_of().range("0", "9").range("a", "f").range("A", "F").end()
        .optional().char("}")
        .end_of_input()
    )
    return as_pattern(chain)


guid = _build()
"""Callable :class:`Pattern` that validates the Microsoft-flavour GUID shape:
the 8-4-4-4-12 hex form (either case) optionally wrapped in braces.
"""

del _build
