"""Shared iterator over the internal element tree.

Provides a single depth-first walker that yields every :class:`BaseElement`
in an emission-order tree, including nested children reachable through
dataclass fields. Callers that need to inspect an entire pattern (ReDoS
detection, serialization, introspection) reuse this instead of hand-rolling
their own traversal.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import fields
from typing import cast

from edify.elements.types.base import BaseElement


def walk_elements(roots: Iterable[BaseElement]) -> Iterator[BaseElement]:
    """Yield every :class:`BaseElement` reachable from ``roots`` in depth-first emission order.

    Each root is yielded first, then its descendants (in dataclass-field order),
    then the next root.

    Args:
        roots: An iterable of root elements.
    """
    for element in roots:
        yield from _walk_single(element)


def _walk_single(element: BaseElement) -> Iterator[BaseElement]:
    yield element
    for spec in fields(element):
        value: object = getattr(element, spec.name)
        if isinstance(value, BaseElement):
            yield from _walk_single(value)
            continue
        if isinstance(value, tuple):
            narrowed_tuple = cast(tuple[BaseElement, ...], value)
            for child in narrowed_tuple:
                yield from _walk_single(child)
