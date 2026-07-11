"""``ssn`` — US Social Security Number shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import Pattern, any_of

_blocked_area = any_of(
    Pattern().string("666"),
    Pattern().string("000"),
    Pattern().char("9").exactly(2).digit(),
)

ssn = (
    Pattern()
    .start_of_input()
    .assert_not_ahead()
    .subexpression(_blocked_area)
    .end()
    .exactly(3).digit()
    .char("-")
    .assert_not_ahead().string("00").end()
    .exactly(2).digit()
    .char("-")
    .assert_not_ahead().exactly(4).char("0").end()
    .exactly(4).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` that validates the US ``AAA-GG-SSSS`` SSN shape
with the documented blocked ranges (``000``, ``666``, ``9xx`` area; ``00``
group; ``0000`` serial).
"""

del _blocked_area