"""``ascii`` — printable-ASCII string shape."""

from __future__ import annotations

from edify import Pattern

ascii = Pattern().start_of_input().one_or_more().range("\x20", "\x7e").end_of_input()
"""Callable :class:`Pattern` for a printable-ASCII-only string
(``0x20``-``0x7E`` — space through tilde).
"""
