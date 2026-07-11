"""``digest`` — content-addressable digest shape."""

from __future__ import annotations

from edify import Pattern

digest = (
    Pattern()
    .start_of_input()
    .group()
    .any_of()
    .string("sha256")
    .string("sha512")
    .string("sha1")
    .string("md5")
    .subexpression(Pattern().string("blake2").optional().any_of_chars("bs"))
    .end()
    .end()
    .any_of_chars(":-")
    .between(32, 128)
    .any_of()
    .range("a", "f")
    .range("A", "F")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a content-addressable digest."""
