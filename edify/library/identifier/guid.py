"""``guid`` — Microsoft-flavour GUID 8-4-4-4-12 hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import Pattern

guid = (
    Pattern()
    .start_of_input()
    .optional()
    .char("{")
    .exactly(8)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .char("-")
    .exactly(4)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .char("-")
    .exactly(4)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .char("-")
    .exactly(4)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .char("-")
    .exactly(12)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .optional()
    .char("}")
    .end_of_input()
)
"""Callable :class:`Pattern` for the Microsoft-flavour GUID 8-4-4-4-12 hex shape.

Guarantees:
    * 32 hex digits in 8-4-4-4-12 layout with hyphen separators.
    * Either case is accepted; the braces are optional and independent.
    * Anchored at both ends.

Does not guarantee:
    * Balanced-brace enforcement — a leading ``{`` without a trailing ``}`` and vice
      versa both pass. Use :data:`edify.library.uuid` for the version- and variant-locked
      RFC 4122 form, or validate braces separately if you require them matched.
    * Version or variant digit values — every hex digit passes.
"""
