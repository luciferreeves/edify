"""``uuid`` — canonical UUID 8-4-4-4-12 hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import Pattern

uuid = (
    Pattern()
    .start_of_input()
    .exactly(8)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .char("-")
    .exactly(4)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .char("-")
    .range("0", "5")
    .exactly(3)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .char("-")
    .any_of_chars("089ab")
    .exactly(3)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .char("-")
    .exactly(12)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the canonical UUID 8-4-4-4-12 lowercase-hex shape.

Guarantees:
    * Exactly 32 lowercase hex digits arranged 8-4-4-4-12 with hyphen separators.
    * Version digit pinned to ``1``-``5`` and variant digit pinned to ``8``-``b``.
    * Anchored at both ends.

Does not guarantee:
    * Uppercase hex — use :data:`edify.library.guid` if either case is required.
    * Brace-wrapped, urn-prefixed, or version-6/7/8 UUIDs.
"""
