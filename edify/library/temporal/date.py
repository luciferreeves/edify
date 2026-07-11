"""``date`` — calendar-date shape (multiple accepted forms)."""

from __future__ import annotations

from edify import Pattern, any_of

_d1 = Pattern().between(1, 2).digit().char("/").between(1, 2).digit().char("/").exactly(4).digit()
_d2 = Pattern().exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
_d3 = Pattern().exactly(2).digit().char("-").exactly(2).digit().char("-").exactly(4).digit()
_d4 = Pattern().exactly(4).digit().char("/").exactly(2).digit().char("/").exactly(2).digit()
_d5 = Pattern().between(1, 2).digit().char(".").between(1, 2).digit().char(".").exactly(4).digit()
_d6 = Pattern().exactly(4).digit().char(".").exactly(2).digit().char(".").exactly(2).digit()
_d7 = Pattern().exactly(8).digit()

date = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_d1, _d2, _d3, _d4, _d5, _d6, _d7))
    .end_of_input()
)
"""Callable :class:`Pattern` for calendar-date shapes:
``M/D/YYYY``, ``YYYY-MM-DD``, ``DD-MM-YYYY``, ``YYYY/MM/DD``,
``DD.MM.YYYY``, ``YYYY.MM.DD``, or ``YYYYMMDD``.
"""
