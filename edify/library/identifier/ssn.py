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
    .exactly(3)
    .digit()
    .char("-")
    .assert_not_ahead()
    .string("00")
    .end()
    .exactly(2)
    .digit()
    .char("-")
    .assert_not_ahead()
    .exactly(4)
    .char("0")
    .end()
    .exactly(4)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the US ``AAA-GG-SSSS`` Social Security Number shape.

Guarantees:
    * Three-digit area, two-digit group, four-digit serial, hyphen-separated.
    * Documented blocked ranges rejected: ``000`` / ``666`` / ``9xx`` area, ``00``
      group, ``0000`` serial.
    * Anchored at both ends.

Does not guarantee:
    * Assignment or issuance history — a shape that clears the blocked ranges may
      still be unassigned.
    * Non-US national identifiers (SIN, NIN, DNI, etc.) — those need dedicated
      validators.
"""

del _blocked_area
