""":class:`Regex` — composition wrapper over :class:`re.Pattern`.

:class:`re.Pattern` is a CPython C type and cannot be subclassed, so we
compose: :class:`Regex` holds both the source string and the compiled
:class:`re.Pattern`, exposing them as ``.source`` and ``.compiled``, and
delegates the eight canonical query methods (``match``, ``search``,
``fullmatch``, ``findall``, ``finditer``, ``sub``, ``subn``, ``split``)
to the underlying compiled pattern.

This wrapper is what :meth:`edify.builder.mixins.terminals.TerminalsMixin.to_regex`
returns; the raw :class:`re.Pattern` is still available via ``.compiled``.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Iterator


class Regex:
    """A compiled edify pattern; wraps :class:`re.Pattern` by composition."""

    def __init__(self, source: str, compiled: re.Pattern[str]) -> None:
        self._source = source
        self._compiled = compiled

    @property
    def source(self) -> str:
        """The regex string that produced this wrapper (identical to :meth:`re.Pattern.pattern`)."""
        return self._source

    @property
    def compiled(self) -> re.Pattern[str]:
        """The underlying :class:`re.Pattern`; callers that need identity checks read this."""
        return self._compiled

    def match(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.match`."""
        return self._compiled.match(string, pos, endpos)

    def search(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.search`."""
        return self._compiled.search(string, pos, endpos)

    def fullmatch(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.fullmatch`."""
        return self._compiled.fullmatch(string, pos, endpos)

    def findall(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> list[str] | list[tuple[str, ...]]:
        """Delegate to :meth:`re.Pattern.findall`."""
        return self._compiled.findall(string, pos, endpos)

    def finditer(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> Iterator[re.Match[str]]:
        """Delegate to :meth:`re.Pattern.finditer`."""
        return self._compiled.finditer(string, pos, endpos)

    def sub(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
    ) -> str:
        """Delegate to :meth:`re.Pattern.sub`."""
        return self._compiled.sub(replacement, string, count=count)

    def subn(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
    ) -> tuple[str, int]:
        """Delegate to :meth:`re.Pattern.subn`."""
        return self._compiled.subn(replacement, string, count=count)

    def split(self, string: str, maxsplit: int = 0) -> list[str | None]:
        """Delegate to :meth:`re.Pattern.split`."""
        return self._compiled.split(string, maxsplit=maxsplit)

    def __repr__(self) -> str:
        """Return ``<Regex 'source-string'>``."""
        return f"<Regex {self._source!r}>"

    def __eq__(self, other: object) -> bool:
        """Return True when ``other`` is a Regex whose source and flags match."""
        if not isinstance(other, Regex):
            return NotImplemented
        return self._source == other._source and self._compiled.flags == other._compiled.flags

    def __hash__(self) -> int:
        """Return a hash derived from the source and compiled flags."""
        return hash((self._source, self._compiled.flags))