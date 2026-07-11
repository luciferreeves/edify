"""``path`` — filesystem path shape (POSIX or Windows)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

path = RegexBackedPattern(
    r"^(?:"
    r"(?:/|(?:\./|(?:\.\./)+))?(?:[^\0\r\n/]+/?)+"
    r"|[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\?)+"
    r"|\\\\[^\\/:*?\"<>|\r\n]+\\[^\\/:*?\"<>|\r\n]+(?:\\[^\\/:*?\"<>|\r\n]*)*"
    r")$"
)
"""Callable :class:`Pattern` for a filesystem path shape: POSIX
(``/absolute`` or ``relative/``), Windows drive-letter, or UNC.
"""
