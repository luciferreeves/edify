"""``path`` — filesystem path shape (POSIX or Windows)."""

from __future__ import annotations

from edify import Pattern, any_of

_posix = (
    Pattern()
    .optional()
    .group()
    .any_of()
    .char("/")
    .group()
    .string("./")
    .end()
    .group()
    .one_or_more()
    .string("../")
    .end()
    .end()
    .end()
    .one_or_more()
    .group()
    .one_or_more()
    .anything_but_chars("\x00\r\n/")
    .optional()
    .char("/")
    .end()
)
_windows = (
    Pattern()
    .letter()
    .string(":\\")
    .one_or_more()
    .group()
    .one_or_more()
    .anything_but_chars("\\/:*?\"<>|\r\n")
    .optional()
    .char("\\")
    .end()
)
_unc = (
    Pattern()
    .string("\\\\")
    .one_or_more()
    .anything_but_chars("\\/:*?\"<>|\r\n")
    .char("\\")
    .one_or_more()
    .anything_but_chars("\\/:*?\"<>|\r\n")
    .zero_or_more()
    .group()
    .char("\\")
    .zero_or_more()
    .anything_but_chars("\\/:*?\"<>|\r\n")
    .end()
)

path = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_posix, _windows, _unc))
    .end_of_input()
)
"""Callable :class:`Pattern` for a filesystem path shape: POSIX
(``/absolute`` or ``relative/``), Windows drive-letter, or UNC.
"""
