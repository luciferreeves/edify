"""``semver`` — SemVer 2.0.0 version shape."""

from __future__ import annotations

from edify import Pattern, any_of


def _positive() -> Pattern:
    return any_of(
        Pattern().char("0"),
        Pattern().range("1", "9").zero_or_more().digit(),
    )


def _pre_id() -> Pattern:
    return any_of(
        Pattern().char("0"),
        Pattern().range("1", "9").zero_or_more().digit(),
        (
            Pattern()
            .zero_or_more()
            .digit()
            .any_of()
            .range("a", "z")
            .range("A", "Z")
            .char("-")
            .end()
            .zero_or_more()
            .any_of()
            .range("0", "9")
            .range("a", "z")
            .range("A", "Z")
            .char("-")
            .end()
        ),
    )


semver = (
    Pattern()
    .start_of_input()
    .named_capture("major")
    .subexpression(_positive())
    .end()
    .char(".")
    .named_capture("minor")
    .subexpression(_positive())
    .end()
    .char(".")
    .named_capture("patch")
    .subexpression(_positive())
    .end()
    .optional()
    .group()
    .char("-")
    .named_capture("prerelease")
    .subexpression(_pre_id())
    .zero_or_more()
    .group()
    .char(".")
    .subexpression(_pre_id())
    .end()
    .end()
    .end()
    .optional()
    .group()
    .char("+")
    .named_capture("buildmetadata")
    .one_or_more()
    .any_of()
    .range("0", "9")
    .range("a", "z")
    .range("A", "Z")
    .char("-")
    .end()
    .zero_or_more()
    .group()
    .char(".")
    .one_or_more()
    .any_of()
    .range("0", "9")
    .range("a", "z")
    .range("A", "Z")
    .char("-")
    .end()
    .end()
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for SemVer 2.0.0 versions."""
