"""``bearer`` — HTTP bearer-token header shape (``Bearer <token>``)."""

from __future__ import annotations

from edify import Pattern

bearer = (
    Pattern()
    .start_of_input()
    .string("Bearer ")
    .one_or_more()
    .any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("._-").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ``Bearer <token>`` HTTP header shape."""
