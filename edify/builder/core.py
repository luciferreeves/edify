"""Shared immutable-state plumbing for :class:`RegexBuilder` and :class:`Pattern`."""

from __future__ import annotations

from typing import Self

from edify.builder.diagnose import diagnose_unfinished
from edify.builder.types.state import BuilderState
from edify.errors.comparison import (
    CannotCompareUnfinishedBuilderError,
    CannotHashUnfinishedBuilderError,
)
from edify.errors.quantifier import DanglingQuantifierError
from edify.errors.structure import CannotCallSubexpressionError
from edify.result.regex import Regex

_UNCLOSED_FRAME_MARKER = "<unclosed>"


class BuilderCore:
    """Holds the immutable :class:`BuilderState` and clones it on chain steps."""

    _state: BuilderState
    _cached_regex: Regex | None

    def __init__(self) -> None:
        self._state = BuilderState()
        self._cached_regex = None

    def _with_state(self, new_state: BuilderState) -> Self:
        """Return a fresh instance of the same concrete type carrying ``new_state``."""
        concrete_class = type(self)
        new_instance = concrete_class.__new__(concrete_class)
        new_instance._state = new_state
        new_instance._cached_regex = None
        return new_instance

    def _lazy_regex(self) -> Regex:
        """Return the memoised :class:`Regex` for this builder, compiling once on first call."""
        cached = self._cached_regex
        if cached is None:
            to_regex = self.to_regex
            cached = to_regex()
            self._cached_regex = cached
        return cached

    def fork(self) -> Self:
        """Return a fresh builder with the same immutable state."""
        return self._with_state(self._state)

    def copy(self) -> Self:
        """Alias for :meth:`fork` — return a fresh builder with the same immutable state."""
        return self._with_state(self._state)

    def __repr__(self) -> str:
        """Return ``<ClassName 'pattern-so-far'>`` for interactive display."""
        rendered = _render_or_marker(self)
        return f"<{type(self).__name__} {rendered!r}>"

    def __eq__(self, other: object) -> bool:
        """Return True when ``other`` is a builder with the same emitted pattern and flags."""
        if not isinstance(other, BuilderCore):
            return NotImplemented
        problems: list = []
        left_problem = diagnose_unfinished(self._state, "left operand")
        right_problem = diagnose_unfinished(other._state, "right operand")
        if left_problem is not None:
            problems.append(left_problem)
        if right_problem is not None:
            problems.append(right_problem)
        if problems:
            raise CannotCompareUnfinishedBuilderError(problems)
        self_source = self.to_regex_string()
        other_source = other.to_regex_string()
        return self_source == other_source and self._state.flags == other._state.flags

    def __hash__(self) -> int:
        """Return a hash derived from ``(emitted_pattern, flags)``."""
        problem = diagnose_unfinished(self._state, "builder")
        if problem is not None:
            raise CannotHashUnfinishedBuilderError(problem)
        source = self.to_regex_string()
        return hash((source, self._state.flags))


def _render_or_marker(builder: BuilderCore) -> str:
    """Return the emitted regex string, or a placeholder when frames are unclosed."""
    to_regex_string = getattr(builder, "to_regex_string", None)
    if to_regex_string is None:
        return _UNCLOSED_FRAME_MARKER
    try:
        return to_regex_string()
    except (CannotCallSubexpressionError, DanglingQuantifierError):
        return _UNCLOSED_FRAME_MARKER
