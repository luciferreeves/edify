"""``avro`` — Avro object-container file signature shape."""

from __future__ import annotations

from edify import Pattern

avro = (
    Pattern().start_of_input().string("Obj\x01").zero_or_more().any_char().end_of_input().dot_all()
)
"""Callable :class:`Pattern` for an Avro object-container file (``Obj\\x01``
magic prefix).
"""
