"""The :class:`MatcherMixin` — direct :mod:`re` method proxies on any fluent surface.

Compiles ``self`` lazily via ``self.to_regex()`` on every call and delegates
to the returned :class:`re.Pattern`. Adding this mixin to a class lets users
write ``pattern.match("10001")`` instead of ``pattern.to_regex().match("10001")``.

The signatures mirror :class:`re.Pattern` exactly so IDE autocomplete and
type inference stay unchanged. :meth:`test` is the one non-:mod:`re` method:
a boolean shortcut that returns ``True`` when the pattern matches anywhere
in the input, ``False`` otherwise.
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
        return self.to_regex().search(string, pos, endpos) is not None

    def match(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.match`."""
        return self.to_regex().match(string, pos, endpos)

    def search(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.search`."""
        return self.to_regex().search(string, pos, endpos)

    def fullmatch(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.fullmatch`."""
        return self.to_regex().fullmatch(string, pos, endpos)

    def findall(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> list[str] | list[tuple[str, ...]]:
        """Delegate to :meth:`re.Pattern.findall`."""
        return self.to_regex().findall(string, pos, endpos)

    def finditer(
        self, string: str, pos: int = 0, endpos: int = sys.maxsize
    ) -> Iterator[re.Match[str]]:
        """Delegate to :meth:`re.Pattern.finditer`."""
        return self.to_regex().finditer(string, pos, endpos)

    def sub(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
    ) -> str:
        """Delegate to :meth:`re.Pattern.sub`."""
        return self.to_regex().sub(replacement, string, count=count)

    def subn(
        self,
        replacement: str | Callable[[re.Match[str]], str],
        string: str,
        count: int = 0,
    ) -> tuple[str, int]:
        """Delegate to :meth:`re.Pattern.subn`."""
        return self.to_regex().subn(replacement, string, count=count)

    def split(self, string: str, maxsplit: int = 0) -> list[str | None]:
        """Delegate to :meth:`re.Pattern.split`."""
        return self.to_regex().split(string, maxsplit=maxsplit)
