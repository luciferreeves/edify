"""The :class:`Regex` composition wrapper over :class:`re.Pattern`."""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Iterator, Mapping

from edify.elements.types.base import BaseElement
from edify.introspect.explain import explain_elements
from edify.introspect.verbose import verbose_elements
from edify.introspect.visualize import visualize_elements

_RePatternMethodReturn = (
    re.Match[str]
    | list[str]
    | list[tuple[str, ...]]
    | Iterator[re.Match[str]]
    | str
    | tuple[str, int]
    | list[str | None]
    | None
)

_RePatternAttribute = int | str | Mapping[str, int] | Callable[..., _RePatternMethodReturn]


class Regex:
    """A compiled edify pattern; wraps :class:`re.Pattern` by composition."""

    def __init__(
        self,
        source: str,
        compiled: re.Pattern[str],
        elements: tuple[BaseElement, ...] = (),
    ) -> None:
        self._source = source
        self._compiled = compiled
        self._elements = elements

    @property
    def source(self) -> str:
        """The regex string this wrapper was built from."""
        return self._source

    @property
    def compiled(self) -> re.Pattern[str]:
        """The underlying :class:`re.Pattern` for direct interop with :mod:`re`."""
        return self._compiled

    @property
    def elements(self) -> tuple[BaseElement, ...]:
        """The AST elements produced by the builder, in emission order."""
        return self._elements

    def match(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> re.Match[str] | None:
        """Delegate to :meth:`re.Pattern.match`."""
        return self._compiled.match(string, pos, endpos)

    def search(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> re.Match[str] | None:
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

    def __getattr__(self, name: str) -> _RePatternAttribute:
        """Return the underlying :class:`re.Pattern` attribute named ``name``."""
        return getattr(self._compiled, name)

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
