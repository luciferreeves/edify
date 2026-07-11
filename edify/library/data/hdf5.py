"""``hdf5`` — hdf5 data-format / file-marker shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

hdf5 = RegexBackedPattern(r"^[A-Za-z0-9_.\-/+]{2,256}$")
"""Callable :class:`Pattern` for hdf5 data-format identifier or content marker."""
