"""Type aliases and Protocols used across the edify compile path."""

from __future__ import annotations

import re
from collections.abc import Callable
from typing import Protocol

from edify.elements.types.base import BaseElement

ElementRenderer = Callable[[BaseElement], str]


class RegexModule(Protocol):
    """The subset of the third-party ``regex`` module surface the backend uses."""

    def compile(self, pattern: str, flags: int = ...) -> re.Pattern[str]: ...
