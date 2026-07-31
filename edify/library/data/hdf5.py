"""``hdf5`` — HDF5 file signature shape."""

from __future__ import annotations

from edify import Pattern

hdf5 = (
    Pattern()
    .start_of_input()
    .string("\x89HDF\r\n\x1a\n")
    .zero_or_more()
    .any_char()
    .end_of_input()
    .dot_all()
)
"""Callable :class:`Pattern` for an HDF5 file (``\\x89HDF\\r\\n\\x1a\\n`` magic
prefix).
"""
