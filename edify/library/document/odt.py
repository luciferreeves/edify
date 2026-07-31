"""``odt`` — OpenDocument text package signature shape."""

from __future__ import annotations

from edify import Pattern

odt = (
    Pattern()
    .start_of_input()
    .string("PK\x03\x04")
    .zero_or_more()
    .any_char()
    .string("application/vnd.oasis.opendocument.text")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an OpenDocument text package: a ZIP container
declaring the ``application/vnd.oasis.opendocument.text`` media type.
"""
