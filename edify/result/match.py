"""The :class:`Match` composition wrapper — attribute-access for named captures."""

from __future__ import annotations

import re
from typing import cast


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
    """A wrapped :class:`re.Match` with attribute-access for named captures.

    Explicitly forwards every :class:`re.Match` method and attribute users typically
    reach for, plus a ``captures`` namespace that exposes named groups by attribute
    access. The underlying :class:`re.Match` stays reachable via :attr:`wrapped`
    for anything not forwarded.
    """

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

    def group(self, *group_selectors: str | int) -> str | tuple[str | None, ...] | None:
        """Delegate to :meth:`re.Match.group`."""
        return self._wrapped_match.group(*group_selectors)

    def groups(self, default: str | None = None) -> tuple[str | None, ...]:
        """Delegate to :meth:`re.Match.groups`."""
        if default is None:
            return self._wrapped_match.groups()
        return self._wrapped_match.groups(default=default)

    def groupdict(self, default: str | None = None) -> dict[str, str | None]:
        """Delegate to :meth:`re.Match.groupdict`."""
        raw_dictionary = self._wrapped_match.groupdict(default=cast(None, default))
        return raw_dictionary

    def start(self, group_selector: str | int = 0) -> int:
        """Delegate to :meth:`re.Match.start`."""
        return self._wrapped_match.start(group_selector)

    def end(self, group_selector: str | int = 0) -> int:
        """Delegate to :meth:`re.Match.end`."""
        return self._wrapped_match.end(group_selector)

    def span(self, group_selector: str | int = 0) -> tuple[int, int]:
        """Delegate to :meth:`re.Match.span`."""
        return self._wrapped_match.span(group_selector)

    def expand(self, template: str) -> str:
        """Delegate to :meth:`re.Match.expand`."""
        return self._wrapped_match.expand(template)

    @property
    def re(self) -> re.Pattern[str]:
        """The compiled pattern that produced this match."""
        return self._wrapped_match.re

    @property
    def string(self) -> str:
        """The string the match ran against."""
        return self._wrapped_match.string

    @property
    def pos(self) -> int:
        """Search start position."""
        return self._wrapped_match.pos

    @property
    def endpos(self) -> int:
        """Search end position."""
        return self._wrapped_match.endpos

    @property
    def lastindex(self) -> int | None:
        """Last matched group index, or None."""
        return self._wrapped_match.lastindex

    @property
    def lastgroup(self) -> str | None:
        """Last matched group name, or None."""
        return self._wrapped_match.lastgroup

    def __getattr__(self, name: str) -> str | None:
        """Return the named-group substring for ``name`` when it's a declared group."""
        wrapped = self._wrapped_match
        group_index_map = wrapped.re.groupindex
        if name in group_index_map:
            return wrapped.group(name)
        raise AttributeError(
            f"{type(self).__name__!r} has no attribute {name!r}; "
            f"declared named groups are {sorted(group_index_map)}"
        )

    def __repr__(self) -> str:
        """Return ``<Match 'span'-'text'>`` for interactive display."""
        return f"<Match {self._wrapped_match.span()} {self._wrapped_match.group()!r}>"
