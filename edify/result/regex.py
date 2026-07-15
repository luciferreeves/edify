"""The :class:`Regex` composition wrapper over the compiled backend pattern."""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Iterator, Mapping
from typing import Any, cast

from edify.builder.types.engine import Engine
from edify.elements.types.base import BaseElement
from edify.errors.backend import TimeoutNotSupportedByEngineError
from edify.introspect.explain import explain_elements
from edify.introspect.verbose import verbose_elements
from edify.introspect.visualize import visualize_elements
from edify.result.match import Match

_MethodReturn = (
    Match
    | list[str]
    | list[tuple[str, ...]]
    | Iterator[Match]
    | str
    | tuple[str, int]
    | list[str | None]
    | None
)

_PatternAttribute = int | str | Mapping[str, int] | Callable[..., _MethodReturn]


class Regex:
    """A compiled edify pattern; wraps the selected engine's ``Pattern`` by composition."""

    def __init__(
        self,
        source: str,
        compiled: Any,
        elements: tuple[BaseElement, ...] = (),
        engine: Engine = "re",
    ) -> None:
        self._source: str = source
        self._compiled: re.Pattern[str] = cast(re.Pattern[str], compiled)
        self._elements: tuple[BaseElement, ...] = elements
        self._engine: Engine = engine

    @property
    def source(self) -> str:
        """The regex string this wrapper was built from."""
        return self._source

    @property
    def compiled(self) -> re.Pattern[str]:
        """The underlying compiled ``Pattern`` for direct interop with the engine module."""
        return self._compiled

    @property
    def elements(self) -> tuple[BaseElement, ...]:
        """The AST elements produced by the builder, in emission order."""
        return self._elements

    @property
    def engine(self) -> Engine:
        """The engine identifier this pattern was compiled with."""
        return self._engine

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Match | None:
        """Delegate to the compiled pattern's ``match`` method."""
        raw = self._compiled.match(string, pos, endpos, **_timeout_kwargs(self._engine, timeout))
        return Match(raw) if raw is not None else None

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Match | None:
        """Delegate to the compiled pattern's ``search`` method."""
        raw = self._compiled.search(string, pos, endpos, **_timeout_kwargs(self._engine, timeout))
        return Match(raw) if raw is not None else None

    def fullmatch(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Match | None:
        """Delegate to the compiled pattern's ``fullmatch`` method."""
        raw = self._compiled.fullmatch(
            string, pos, endpos, **_timeout_kwargs(self._engine, timeout)
        )
        return Match(raw) if raw is not None else None

    def findall(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> list[str] | list[tuple[str, ...]]:
        """Delegate to the compiled pattern's ``findall`` method."""
        return self._compiled.findall(string, pos, endpos, **_timeout_kwargs(self._engine, timeout))

    def finditer(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Iterator[Match]:
        """Delegate to the compiled pattern's ``finditer`` method."""
        raw_iter = self._compiled.finditer(
            string, pos, endpos, **_timeout_kwargs(self._engine, timeout)
        )
        for raw in raw_iter:
            yield Match(raw)

    def sub(
        self,
        replacement: str | Callable[[Match], str],
        string: str,
        count: int = 0,
        *,
        timeout: float | None = None,
    ) -> str:
        """Delegate to the compiled pattern's ``sub`` method."""
        adapter = _wrap_replacement(replacement)
        return self._compiled.sub(
            adapter, string, count=count, **_timeout_kwargs(self._engine, timeout)
        )

    def subn(
        self,
        replacement: str | Callable[[Match], str],
        string: str,
        count: int = 0,
        *,
        timeout: float | None = None,
    ) -> tuple[str, int]:
        """Delegate to the compiled pattern's ``subn`` method."""
        adapter = _wrap_replacement(replacement)
        return self._compiled.subn(
            adapter, string, count=count, **_timeout_kwargs(self._engine, timeout)
        )

    def split(
        self,
        string: str,
        maxsplit: int = 0,
        *,
        timeout: float | None = None,
    ) -> list[str | None]:
        """Delegate to the compiled pattern's ``split`` method."""
        return self._compiled.split(
            string, maxsplit=maxsplit, **_timeout_kwargs(self._engine, timeout)
        )

    def explain(self) -> str:
        """Return a human-readable narrative describing what the pattern matches."""
        return explain_elements(self._elements)

    def to_verbose_string(self) -> str:
        """Return the pattern as an annotated ``re.VERBOSE``-compatible string."""
        return verbose_elements(self._elements)

    def visualize(self, format: str = "ascii", engine: str = "ascii") -> str:
        """Return a visual rendering of the pattern in ``format``.

        Args:
            format: ``"ascii"`` (default) for an ASCII railroad diagram, or
                ``"svg"`` for a Graphviz-rendered SVG string.
            engine: Rendering engine identifier; ``"ascii"`` for the built-in
                ASCII layout, ``"graphviz"`` for the SVG renderer. Must match
                ``format``.

        Returns:
            The rendered diagram as a string.

        Raises:
            edify.errors.introspect.UnsupportedVisualizationFormatError: when
                ``format`` is not one of ``"ascii"`` or ``"svg"``.
            edify.errors.introspect.UnsupportedVisualizationEngineError: when
                ``engine`` does not match the requested ``format``.
            edify.errors.introspect.MissingGraphvizDependencyError: when
                ``format="svg"`` is requested but the ``graphviz`` extra is
                not installed.
        """
        return visualize_elements(self._elements, format=format, engine=engine)

    def __getattr__(self, name: str) -> _PatternAttribute:
        """Return the underlying compiled pattern's attribute named ``name``."""
        attribute: _PatternAttribute = getattr(self._compiled, name)
        return attribute

    def __repr__(self) -> str:
        """Return ``<Regex 'source-string'>``."""
        return f"<Regex {self._source!r}>"

    def __eq__(self, other: object) -> bool:
        """Return True when ``other`` is a Regex whose source, engine, and flags match."""
        if not isinstance(other, Regex):
            return NotImplemented
        return (
            self._source == other._source
            and self._engine == other._engine
            and self._compiled.flags == other._compiled.flags
        )

    def __hash__(self) -> int:
        """Return a hash derived from the source, engine, and compiled flags."""
        return hash((self._source, self._engine, self._compiled.flags))


def _timeout_kwargs(engine: Engine, timeout: float | None) -> Mapping[str, float]:
    if timeout is None:
        return {}
    if engine == "re":
        raise TimeoutNotSupportedByEngineError()
    return {"timeout": timeout}


def _wrap_replacement(
    replacement: str | Callable[[Match], str],
) -> str | Callable[[re.Match[str]], str]:
    if isinstance(replacement, str):
        return replacement
    caller = replacement

    def adapter(raw_match: re.Match[str]) -> str:
        return caller(Match(raw_match))

    return adapter
