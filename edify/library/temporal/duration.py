"""``duration`` — ISO 8601 duration shape (``PnYnMnDTnHnMnS``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

duration = RegexBackedPattern(
    r"^P(?!$)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?"
    r"(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?"
    r"(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?"
    r"(?:\d+(?:\.\d+)?S)?)?$"
)
"""Callable :class:`Pattern` for the ISO 8601 duration shape:
``PnYnMnDTnHnMnS`` with optional fractional components.
"""
