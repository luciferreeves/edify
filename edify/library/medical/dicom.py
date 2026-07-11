"""``dicom`` — DICOM UID shape (dotted digits)."""

from __future__ import annotations

from edify import Pattern

dicom = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .digit()
    .one_or_more()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a DICOM UID: dotted-integer chain."""
