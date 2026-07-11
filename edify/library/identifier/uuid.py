"""``uuid`` — canonical UUID 8-4-4-4-12 hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import RegexBuilder
from edify.library._support.atoms import hex_lower
from edify.library._support.coerce import as_pattern


def _build() -> object:
    chain = (
        RegexBuilder()
        .start_of_input()
        .exactly(8).any_of().range("0", "9").range("a", "f").end()
        .char("-")
        .exactly(4).any_of().range("0", "9").range("a", "f").end()
        .char("-")
        .range("0", "5")
        .exactly(3).any_of().range("0", "9").range("a", "f").end()
        .char("-")
        .any_of_chars("089ab")
        .exactly(3).any_of().range("0", "9").range("a", "f").end()
        .char("-")
        .exactly(12).any_of().range("0", "9").range("a", "f").end()
        .end_of_input()
    )
    return as_pattern(chain)


uuid = _build()
"""Callable :class:`Pattern` that validates the canonical UUID 8-4-4-4-12
lowercase-hex shape with the version digit pinned to ``1``–``5`` and the
variant digit pinned to ``8``–``b``.
"""

del _build, hex_lower
