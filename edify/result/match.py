"""The :class:`Match` composition wrapper — attribute-access for named captures."""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Any


class NamedCaptures:
    """A namespace exposing every named capture group as an attribute."""

    def __init__(self, wrapped_match: re.Match[str]) -> None:
        self._wrapped_match = wrapped_match

    def __getattr__(self, name: str) -> str | None:
        """Return the substring captured by the named group ``name``."""
        group_index_map = self._wrapped_match.re.groupindex
        if name not in group_index_map:
            raise AttributeError(
                f"named capture group {name!r} does not exist on this pattern; "
                f"declared groups are {sorted(group_index_map)}"
            )
        return self._wrapped_match.group(name)

    def __dir__(self) -> list[str]:
        """Return every declared named group so ``dir()`` and IDE completion see them."""
        return sorted(self._wrapped_match.re.groupindex)


class Match:
    """A wrapped :class:`re.Match` with attribute-access for named captures."""

    def __init__(self, wrapped_match: re.Match[str]) -> None:
        self._wrapped_match: re.Match[str] = wrapped_match
        self._captures: NamedCaptures = NamedCaptures(wrapped_match)

    @property
    def wrapped(self) -> re.Match[str]:
        """The underlying :class:`re.Match` for direct interop with :mod:`re`."""
        return self._wrapped_match

    @property
    def captures(self) -> NamedCaptures:
        """A namespace of named groups; access captures via ``m.captures.<name>``."""
        return self._captures

    def __getattr__(self, name: str) -> Any:
        """Return the named-group substring or delegate to the underlying re.Match."""
        wrapped = self._wrapped_match
        group_index_map = wrapped.re.groupindex
        if name in group_index_map:
            return wrapped.group(name)
        attribute: str | Callable[..., Any] = getattr(wrapped, name)
        return attribute

    def __repr__(self) -> str:
        """Return ``<Match 'span'-'text'>`` for interactive display."""
        return f"<Match {self._wrapped_match.span()} {self._wrapped_match.group()!r}>"
