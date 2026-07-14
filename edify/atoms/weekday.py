"""``weekday`` — day-of-week name (three-letter or full English)."""

from __future__ import annotations

from edify import Pattern, any_of

weekday = any_of(
    Pattern().string("Monday"),
    Pattern().string("Tuesday"),
    Pattern().string("Wednesday"),
    Pattern().string("Thursday"),
    Pattern().string("Friday"),
    Pattern().string("Saturday"),
    Pattern().string("Sunday"),
    Pattern().string("Mon"),
    Pattern().string("Tue"),
    Pattern().string("Wed"),
    Pattern().string("Thu"),
    Pattern().string("Fri"),
    Pattern().string("Sat"),
    Pattern().string("Sun"),
)
"""Composable :class:`Pattern` fragment for an English weekday name."""
