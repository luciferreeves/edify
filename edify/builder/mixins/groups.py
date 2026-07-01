"""The :class:`GroupsMixin` — chain methods for non-capturing groups and alternation.

* :meth:`GroupsMixin.any_of` — dual-mode. Called with no arguments it opens
  an alternation frame that :meth:`.end` closes later; called with literal
  string arguments it appends an :class:`AnyOfElement` built directly from
  those literals (the varargs shorthand for the common case).
* :meth:`GroupsMixin.one_of` — always the varargs form; ``.one_of("a", "b")``
  is the canonical way to alternate between literal strings.
* :meth:`GroupsMixin.group` — opens a non-capturing-group frame that
  :meth:`.end` closes later.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.compile.escape import escape_special
from edify.elements.types.base import BaseElement
from edify.elements.types.chars import CharElement, StringElement
from edify.elements.types.groups import AnyOfElement, GroupElement
from edify.errors.input import (
    MustBeAStringError,
    MustBeAtLeastOneLiteralError,
    MustBeOneCharacterError,
)


class GroupsMixin(BuilderProtocol):
    """Provides the ``any_of``/``one_of``/``group`` chain methods."""

    def any_of(self, *literals: str) -> Self:
        """Return a new builder with alternation appended.

        With no arguments this opens an alternation frame that :meth:`.end`
        closes later. With one or more string arguments each literal is
        wrapped as :class:`CharElement` or :class:`StringElement` and the
        whole set is appended as one :class:`AnyOfElement`.
        """
        if not literals:
            return _open_frame(self, AnyOfElement())
        return _add_literal_alternation(self, literals)

    def one_of(self, *literals: str) -> Self:
        """Return a new builder with a literal ``AnyOfElement`` appended.

        Requires at least one literal; unlike :meth:`any_of` this method
        never opens a frame.
        """
        _ensure_at_least_one_literal(literals)
        return _add_literal_alternation(self, literals)

    def group(self) -> Self:
        """Return a new builder with a non-capturing-group frame opened."""
        return _open_frame(self, GroupElement())


def _open_frame(builder: BuilderProtocol, type_node: BaseElement):
    """Push a new frame anchored at ``type_node`` and return the updated builder."""
    new_frame = StackFrame(type_node=type_node)
    new_state = builder._state.with_frame_pushed(new_frame)
    return builder._with_state(new_state)


def _add_literal_alternation(builder: BuilderProtocol, literals: tuple[str, ...]):
    """Append a single :class:`AnyOfElement` built from ``literals`` to the top frame."""
    children = tuple(_literal_to_element(literal) for literal in literals)
    element = AnyOfElement(children=children)
    new_state = builder._state.with_element_added_to_top(element)
    return builder._with_state(new_state)


def _literal_to_element(literal: str) -> CharElement | StringElement:
    """Validate and escape ``literal``, returning the char- or string-shaped element."""
    _ensure_is_string("Literal", literal)
    _ensure_non_empty("Literal", literal)
    escaped = escape_special(literal)
    if len(literal) == 1:
        return CharElement(value=escaped)
    return StringElement(value=escaped)


def _ensure_is_string(label: str, value: object) -> None:
    """Raise :class:`MustBeAStringError` when ``value`` is not a string."""
    if isinstance(value, str):
        return
    actual_type_name = type(value).__name__
    raise MustBeAStringError(label, actual_type_name)


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
