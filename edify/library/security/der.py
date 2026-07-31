"""``der`` — DER-encoded structure shape."""

from __future__ import annotations

from edify import Pattern

_short_form = Pattern().range("\x00", "\x7f")

_long_form = Pattern().range("\x81", "\x84").one_or_more().any_char()

der = (
    Pattern()
    .start_of_input()
    .char("\x30")
    .any_of()
    .use(_long_form)
    .use(_short_form)
    .end()
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for a DER-encoded structure: a ``SEQUENCE`` tag
followed by a short- or long-form length.
"""
