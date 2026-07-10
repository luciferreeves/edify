"""Dispatch entry point for the :meth:`Regex.visualize` rendering formats."""

from __future__ import annotations

from edify.elements.types.base import BaseElement
from edify.errors.introspect import (
    UnsupportedVisualizationEngineError,
    UnsupportedVisualizationFormatError,
)
from edify.introspect.ascii import render_ascii
from edify.introspect.graphviz import render_graphviz_svg

_FORMAT_ASCII = "ascii"
_FORMAT_SVG = "svg"
_ENGINE_ASCII = "ascii"
_ENGINE_GRAPHVIZ = "graphviz"


def visualize_elements(
    elements: tuple[BaseElement, ...],
    format: str = _FORMAT_ASCII,
    engine: str = _ENGINE_ASCII,
) -> str:
    """Render ``elements`` in the requested ``format`` / ``engine`` combination."""
    if format == _FORMAT_ASCII:
        if engine != _ENGINE_ASCII:
            raise UnsupportedVisualizationEngineError(format, engine)
        return render_ascii(elements)
    if format == _FORMAT_SVG:
        if engine != _ENGINE_GRAPHVIZ:
            raise UnsupportedVisualizationEngineError(format, engine)
        return render_graphviz_svg(elements)
    raise UnsupportedVisualizationFormatError(format)
