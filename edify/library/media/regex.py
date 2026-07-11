"""``regex`` — pattern that itself compiles as a valid regex."""

from __future__ import annotations

import re

from edify.pattern.composition import Pattern


class _RegexPattern(Pattern):
    def __call__(self, value: str) -> bool:
        if not isinstance(value, str):
            return False
        try:
            re.compile(value)
        except re.error:
            return False
        return True


regex = _RegexPattern()
"""Callable :class:`Pattern` that returns True iff ``value`` compiles as
a valid Python regular expression.
"""
