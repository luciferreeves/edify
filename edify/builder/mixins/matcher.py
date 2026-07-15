"""The :class:`MatcherMixin` — direct :mod:`re` method proxies on any fluent surface.

Compiles ``self`` on first use via :meth:`edify.builder.core.BuilderCore._lazy_regex`
and reuses the cached :class:`edify.result.regex.Regex` on every subsequent call,
so ``pattern.test("a")`` followed by ``pattern.match("b")`` compiles the underlying
regex exactly once.

The signatures mirror :class:`re.Pattern` exactly so IDE autocomplete and
type inference stay unchanged. :meth:`test` is the one non-:mod:`re` method:
a boolean shortcut that returns ``True`` when the pattern matches anywhere
in the input, ``False`` otherwise. Every match method also accepts a per-call
``timeout=`` kwarg that only applies under ``engine="regex"``.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Iterator

from edify.builder.types.protocol import BuilderProtocol


class MatcherMixin(BuilderProtocol):
    """Provides nine :class:`re.Pattern` proxy methods plus :meth:`test` on any fluent surface."""

    def test(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> bool:
        """Return ``True`` when the pattern matches anywhere in ``string``, else ``False``."""
        return self._lazy_regex().search(string, pos, endpos) is not None

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.match`."""
        return self._lazy_regex().match(string, pos, endpos, timeout=timeout)

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.search`."""
        return self._lazy_regex().search(string, pos, endpos, timeout=timeout)

    def fullmatch(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.fullmatch`."""
        return self._lazy_regex().fullmatch(string, pos, endpos, timeout=timeout)

    def findall(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> list[str] | list[tuple[str, ...]]:
        """Delegate to :meth:`re.Pattern.findall`."""
        return self._lazy_regex().findall(string, pos, endpos, timeout=timeout)

    def finditer(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Iterator[re.Match[str]]:
        """Delegate to :meth:`re.Pattern.finditer`."""
        return self._lazy_regex().finditer(string, pos, endpos, timeout=timeout)

    def sub(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
        *,
        timeout: float | None = None,
    ) -> str:
        """Delegate to :meth:`re.Pattern.sub`."""
        return self._lazy_regex().sub(replacement, string, count=count, timeout=timeout)

    def subn(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
        *,
        timeout: float | None = None,
    ) -> tuple[str, int]:
        """Delegate to :meth:`re.Pattern.subn`."""
        return self._lazy_regex().subn(replacement, string, count=count, timeout=timeout)

    def split(
        self,
        string: str,
        maxsplit: int = 0,
        *,
        timeout: float | None = None,
    ) -> list[str | None]:
        """Delegate to :meth:`re.Pattern.split`."""
        return self._lazy_regex().split(string, maxsplit=maxsplit, timeout=timeout)
