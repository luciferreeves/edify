"""The :class:`GroupsMixin` — chain methods for non-capturing groups and alternation.

* :meth:`GroupsMixin.any_of` — dual-mode. Called with no arguments it opens
  an alternation frame that :meth:`.end` closes later; called with literal
  string arguments it appends an :class:`AnyOfElement` built directly from
  those literals (the varargs shorthand for the common case).
* :meth:`GroupsMixin.one_of` — always the varargs form; ``.one_of("a", "b")``
  is the canonical way to alternate between literal strings.
* :meth:`GroupsMixin.anything_but_any_of` — opens a negated-character-class
  frame; every member added inside it is rejected rather than accepted.
* :meth:`GroupsMixin.group` — opens a non-capturing-group frame that
  :meth:`.end` closes later.
"""

from __future__ import annotations

from typing import Self, TypeVar

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.compile.escape import escape_special
from edify.elements.types.base import BaseElement
from edify.elements.types.chars import CharElement, StringElement
from edify.elements.types.groups import AnyOfElement, AnythingButAnyOfElement, GroupElement
from edify.errors.input import (
    MustBeAtLeastOneLiteralError,
    MustBeOneCharacterError,
)

_TBuilder = TypeVar("_TBuilder", bound=BuilderProtocol)


class GroupsMixin(BuilderProtocol):
    """Provides the ``any_of``/``one_of``/``group`` chain methods."""

    def any_of(self, *literals: str) -> Self:
        """Return a new builder with alternation appended.

        With no arguments this opens an alternation frame that :meth:`.end`
        closes later. With one or more string arguments each literal is
        wrapped as :class:`CharElement` or :class:`StringElement` and the
        whole set is appended as one :class:`AnyOfElement`.

        Branches are tried left to right and the first to match wins, so a branch that
        prefixes a later one will shadow it unless the pattern is anchored.

        Args:
            *literals: The alternatives, as strings. Pass none to open a frame instead
                and add branches with further chain calls.
        """
        if not literals:
            return _open_frame(self, AnyOfElement())
        return _add_literal_alternation(self, literals)

    def one_of(self, *literals: str) -> Self:
        """Return a new builder with a literal ``AnyOfElement`` appended.

        Requires at least one literal; unlike :meth:`any_of` this method
        never opens a frame.

        Args:
            *literals: The alternatives, as strings. At least one is required.

        Raises:
            MustBeAtLeastOneLiteralError: If no literals are given.
        """
        _ensure_at_least_one_literal(literals)
        return _add_literal_alternation(self, literals)

    def anything_but_any_of(self) -> Self:
        """Return a new builder with a negated-character-class frame opened.

        Add the rejected members with :meth:`.char`, :meth:`.any_of_chars` and
        :meth:`.range`, then close the frame with :meth:`.end`. The result
        matches any single character that is none of them.

        Raises:
            CannotNegateNonCharacterMemberError: At compile time, if the frame
                holds a member wider than a single character.
        """
        return _open_frame(self, AnythingButAnyOfElement())

    def group(self) -> Self:
        """Return a new builder with a non-capturing-group frame opened."""
        return _open_frame(self, GroupElement())


def _open_frame(builder: _TBuilder, type_node: BaseElement) -> _TBuilder:
    """Push a new frame anchored at ``type_node`` and return the updated builder."""
    new_frame = StackFrame(type_node=type_node)
    new_state = builder.state.with_frame_pushed(new_frame)
    return builder.with_state(new_state)


def _add_literal_alternation(builder: _TBuilder, literals: tuple[str, ...]) -> _TBuilder:
    """Append a single :class:`AnyOfElement` built from ``literals`` to the top frame."""
    child_elements = [_literal_to_element(literal) for literal in literals]
    children = tuple(child_elements)
    element = AnyOfElement(children=children)
    new_state = builder.state.with_element_added_to_top(element)
    return builder.with_state(new_state)


def _literal_to_element(literal: str) -> CharElement | StringElement:
    """Validate and escape ``literal``, returning the char- or string-shaped element."""
    _ensure_non_empty("Literal", literal)
    escaped = escape_special(literal)
    if len(literal) == 1:
        return CharElement(value=escaped)
    return StringElement(value=escaped)


def _ensure_non_empty(label: str, value: str) -> None:
    """Raise :class:`MustBeOneCharacterError` when ``value`` has length zero."""
    if len(value) > 0:
        return
    raise MustBeOneCharacterError(label)


def _ensure_at_least_one_literal(literals: tuple[str, ...]) -> None:
    """Raise :class:`MustBeAtLeastOneLiteralError` when ``literals`` is empty."""
    if literals:
        return
    raise MustBeAtLeastOneLiteralError("one_of")
