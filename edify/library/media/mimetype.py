"""``mimetype`` — ``type/subtype`` MIME shape."""

from __future__ import annotations

from edify import Pattern


def _mime_body() -> Pattern:
    return (
        Pattern()
        .letter()
        .zero_or_more()
        .any_of()
        .range("a", "z")
        .range("A", "Z")
        .range("0", "9")
        .char("!")
        .char("#")
        .char("$")
        .char("&")
        .char("-")
        .char("^")
        .char("_")
        .char(".")
        .char("+")
        .end()
    )


mimetype = (
    Pattern()
    .start_of_input()
    .subexpression(_mime_body())
    .char("/")
    .subexpression(_mime_body())
    .end_of_input()
)
"""Callable :class:`Pattern` for the ``type/subtype`` MIME shape."""
