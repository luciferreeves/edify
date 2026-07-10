"""Private base class for validators whose regex is authored as a raw string.

Used by the built-in library validators that carry a regex too dense to author
as a fluent chain (RFC 5322 email, full IPv6 form, etc.). The base class stores
the raw regex string, compiles it once at construction time, and threads it
through :meth:`to_regex_string`, :meth:`to_regex`, and :meth:`__call__` so the
resulting instance is indistinguishable from a fluent-chain :class:`Pattern`
for the purposes of ``isinstance``, ``.match()``, and the ``pattern(value)``
call form.
"""

from __future__ import annotations

import re

from edify.pattern.composition import Pattern
from edify.result.regex import Regex


class RegexBackedPattern(Pattern):
    """A :class:`Pattern` whose emitted regex is a pre-authored raw string.

    Attributes:
        raw_regex_string: The exact regex string emitted by :meth:`to_regex_string`.
    """

    def __init__(self, raw_regex_string: str) -> None:
        super().__init__()
        self._raw_regex_string = raw_regex_string
        self._compiled_regex = re.compile(raw_regex_string)

    @property
    def raw_regex_string(self) -> str:
        """Return the raw regex string this pattern was constructed from."""
        return self._raw_regex_string

    def to_regex_string(self) -> str:
        """Return the raw regex string verbatim."""
        return self._raw_regex_string

    def to_regex(self) -> Regex:
        """Return a :class:`Regex` wrapping the pre-compiled pattern."""
        return Regex(self._raw_regex_string, self._compiled_regex, ())
