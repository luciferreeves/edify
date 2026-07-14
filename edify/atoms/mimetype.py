"""``mimetype`` — ``type/subtype`` MIME identifier."""

from __future__ import annotations

from edify import Pattern


def _token() -> Pattern:
    return (
        Pattern()
        .letter()
        .zero_or_more()
        .any_of()
        .range("a", "z")
        .range("A", "Z")
        .range("0", "9")
        .char("+")
        .char("-")
        .char(".")
        .end()
    )


mimetype = Pattern().use(_token()).char("/").use(_token())
"""Composable :class:`Pattern` fragment for a ``type/subtype`` MIME identifier."""
