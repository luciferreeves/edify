"""Root element — the top of every compiled edify AST.

A :class:`RootElement` wraps the entire ordered list of top-level children
that make up a pattern. The builder starts with an empty root and appends
to it as the user chains methods; the compile path receives a single
:class:`RootElement` and concatenates the rendered fragments of each child.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class RootElement(BaseElement):
    """The wrapper around every top-level child element of a pattern.

    Attributes:
        children: The top-level elements rendered in order to produce the
            final regex string.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)
