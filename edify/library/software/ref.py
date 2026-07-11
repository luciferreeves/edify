"""``ref`` — git ref shape (SHA, ``refs/…``, or bare branch/tag name)."""

from __future__ import annotations

from edify import Pattern, any_of


def _forbidden() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .whitespace_char()
        .any_of_chars("~^:?*[\\")
        .end()
        .end()
        .any_char()
    )


def _forbidden_incl_slash() -> Pattern:
    return (
        Pattern()
        .assert_not_ahead()
        .any_of()
        .whitespace_char()
        .any_of_chars("~^:?*[\\/")
        .end()
        .end()
        .any_char()
    )


_sha = Pattern().between(7, 40).any_of().range("a", "f").range("0", "9").end()
_refs = (
    Pattern()
    .string("refs/")
    .group()
    .any_of()
    .string("heads")
    .string("tags")
    .string("remotes")
    .end()
    .end()
    .char("/")
    .one_or_more()
    .subexpression(_forbidden())
)
_bare = Pattern().subexpression(_forbidden_incl_slash()).between(0, 127).subexpression(_forbidden())

ref = Pattern().start_of_input().subexpression(any_of(_sha, _refs, _bare)).end_of_input()
"""Callable :class:`Pattern` for a git ref: SHA, ``refs/heads/…``, or bare branch/tag name."""
