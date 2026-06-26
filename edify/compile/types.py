"""Type aliases used across the edify compile path."""

from __future__ import annotations

from collections.abc import Callable

from edify.elements.types.base import BaseElement

ElementRenderer = Callable[[BaseElement], str]
