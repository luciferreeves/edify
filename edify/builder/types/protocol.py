"""The :class:`BuilderProtocol` — the contract every mixin assumes about ``self``.

Each mixin defines methods that read ``self.state`` and return a new builder
via ``self.with_state(new_state)``. Typing ``self`` against this protocol
gives both type checkers a complete picture of the cross-mixin attribute
surface even when individual mixin files are inspected in isolation.

The Protocol declares every public chain method that any mixin might call on
``self`` (``.any_of``, ``.end``, ``.subexpression``, etc.). Concrete classes
(``RegexBuilder``, ``Pattern``) get real implementations by composing every
mixin; the Protocol declarations here exist only so a mixin in isolation can
see the surface without pulling in every other mixin at import time.
"""

from __future__ import annotations

from typing import Protocol, Self, runtime_checkable

from edify.builder.types.state import BuilderState
from edify.result.regex import Regex


@runtime_checkable
class BuilderProtocol(Protocol):
    """The shared shape that every builder mixin assumes about ``self``."""

    state: BuilderState
    cached_regex: Regex | None

    def __init__(self) -> None: ...

    def with_state(self, new_state: BuilderState, /) -> Self: ...

    def lazy_regex(self) -> Regex: ...

    def to_regex_string(self) -> str: ...

    def to_regex(self) -> Regex: ...

    def any_of(self, *literals: str) -> Self: ...

    def end(self) -> Self: ...

    def subexpression(
        self,
        expression: BuilderProtocol,
        namespace: str = ...,
        ignore_flags: bool = ...,
        ignore_start_and_end: bool = ...,
    ) -> Self: ...
