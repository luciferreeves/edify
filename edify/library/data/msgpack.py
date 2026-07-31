"""``msgpack`` — MessagePack map or array payload shape."""

from __future__ import annotations

from edify import Pattern

_fixmap = Pattern().range("\x80", "\x8f")
_fixarray = Pattern().range("\x90", "\x9f")
_sized = Pattern().any_of_chars("\xdc\xdd\xde\xdf")

msgpack = (
    Pattern()
    .start_of_input()
    .any_of()
    .use(_fixmap)
    .use(_fixarray)
    .use(_sized)
    .end()
    .one_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a MessagePack payload whose root is a map or an
array, identified by its leading type-tag byte.
"""
