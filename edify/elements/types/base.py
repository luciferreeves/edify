"""Base class shared by every concrete element in the edify AST.

Provides a common type that recursive dataclass fields can reference —
``tuple[BaseElement, ...]`` for capture children, ``BaseElement`` for the
quantifier's single child. Function signatures that consume or return AST
nodes should use the precise :data:`edify.elements.types.Element` union.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BaseElement:
    """Empty marker base class for every concrete element dataclass."""
