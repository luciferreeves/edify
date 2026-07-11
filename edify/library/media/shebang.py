"""``shebang`` — shebang line shape."""

from __future__ import annotations

from edify import Pattern

shebang = (
    Pattern()
    .start_of_input()
    .string("#!/")
    .optional()
    .group()
    .string("usr/")
    .end()
    .group()
    .any_of()
    .string("bin")
    .string("sbin")
    .string("local")
    .end()
    .end()
    .char("/")
    .optional()
    .group()
    .string("env")
    .one_or_more()
    .whitespace_char()
    .end()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("+")
    .char("/")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a shebang line at the top of a script."""
