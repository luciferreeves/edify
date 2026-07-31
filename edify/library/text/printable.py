"""``printable`` — printable ASCII string shape."""

from __future__ import annotations

from edify import Pattern

printable = Pattern().start_of_input().one_or_more().range("\x20", "\x7e").end_of_input()
"""Callable :class:`Pattern` for a printable ASCII string: space through tilde,
excluding every control code.
"""
