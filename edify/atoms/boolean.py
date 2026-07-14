"""``boolean`` — any common boolean spelling (true/false/yes/no/on/off/1/0)."""

from __future__ import annotations

from edify import Pattern, any_of

boolean = any_of(
    Pattern().string("true"),
    Pattern().string("false"),
    Pattern().string("True"),
    Pattern().string("False"),
    Pattern().string("TRUE"),
    Pattern().string("FALSE"),
    Pattern().string("yes"),
    Pattern().string("no"),
    Pattern().string("Yes"),
    Pattern().string("No"),
    Pattern().string("YES"),
    Pattern().string("NO"),
    Pattern().string("on"),
    Pattern().string("off"),
    Pattern().string("On"),
    Pattern().string("Off"),
    Pattern().string("ON"),
    Pattern().string("OFF"),
    Pattern().string("1"),
    Pattern().string("0"),
)
"""Composable :class:`Pattern` fragment for any common boolean spelling."""
