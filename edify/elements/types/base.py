"""Base class shared by every concrete element in the edify AST.

Provides a common type that recursive children can reference
(``tuple[BaseElement, ...]`` for capture children, ``BaseElement`` for the
quantifier's single child) without forcing each module to import the full
:data:`edify.elements.types.Element` union — which would form an import
cycle since the union lists every concrete subclass.

Function signatures that consume or return AST nodes should still use the
precise :data:`Element` union from :mod:`edify.elements.types`; this base
exists only so that the dataclass field annotations type-check without a
circular import.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BaseElement:
    """Empty marker base class for every concrete element dataclass."""
