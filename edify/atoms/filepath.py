"""``filepath`` — a POSIX or Windows file path shape."""

from __future__ import annotations

from edify import Pattern, any_of

_posix = (
    Pattern()
    .optional()
    .char("/")
    .one_or_more()
    .group()
    .anything_but_chars("/\x00")
    .optional()
    .char("/")
    .end()
)
_windows = (
    Pattern()
    .letter()
    .string(":")
    .one_or_more()
    .group()
    .char("\\")
    .anything_but_chars('/\\<>:"|?*\x00\n')
    .end()
)

filepath = any_of(_posix, _windows)
"""Composable :class:`Pattern` fragment for a filesystem path."""
