"""Functional value factories — the free-function counterpart to :class:`CharsMixin`.

Every factory returns a fresh :class:`Pattern` whose root frame holds a
single character-shaped element. Input validation and escaping delegate
to the same helpers the fluent chain uses, so ``string("a.b")`` and
``Pattern().string("a.b")`` behave identically.
"""

from __future__ import annotations

from edify.pattern.composition import Pattern
from edify.pattern.factories.wrap import pattern_containing


def string(value: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing the literal ``value``."""
    return _first_child_pattern(Pattern().string(value))


def char(value: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing the single-character literal ``value``."""
    return _first_child_pattern(Pattern().char(value))


def range_of(start_character: str, end_character: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing a ``[start-end]`` range."""
    return _first_child_pattern(Pattern().range(start_character, end_character))


def chars(characters: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing an inline ``[characters]`` class."""
    return _first_child_pattern(Pattern().any_of_chars(characters))


def nonstring(value: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing a per-character negation of ``value``."""
    return _first_child_pattern(Pattern().anything_but_string(value))


def nonchars(characters: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing an inline ``[^characters]`` negation."""
    return _first_child_pattern(Pattern().anything_but_chars(characters))


def nonrange(start_character: str, end_character: str) -> Pattern:
    """Return a fresh :class:`Pattern` containing a ``[^start-end]`` negated range."""
    return _first_child_pattern(Pattern().anything_but_range(start_character, end_character))


def _first_child_pattern(built: Pattern) -> Pattern:
    """Isolate the element the mixin just appended into its own fresh :class:`Pattern`."""
    return pattern_containing(built.state.top_frame.children[-1])
