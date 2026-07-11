"""``extension`` — file extension shape (``.ext``)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
extension = RegexBackedPattern(r"^\.[a-zA-Z0-9]{1,10}$")
"""Callable :class:`Pattern` for a file extension: dot + 1-10 alphanumeric."""
