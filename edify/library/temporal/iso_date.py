"""``iso_date`` — strict ISO 8601 date shape (``YYYY-MM-DD``)."""

from __future__ import annotations

from edify import Pattern

iso_date = (
    Pattern()
    .start_of_input()
    .exactly(4)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 8601 calendar-date shape ``YYYY-MM-DD``.

Guarantees:
    * Exactly four year digits, two month digits, two day digits.
    * Hyphen separators, no whitespace, no time component.
    * Anchored at both ends.

Does not guarantee:
    * Calendar validity — accepts shapes like ``2026-02-30`` that the ISO
      grammar allows but the calendar does not.
    * ISO 8601 time or datetime shapes — use :data:`edify.library.datetime`
      for those.
"""
