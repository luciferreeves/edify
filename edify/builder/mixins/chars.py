"""The :class:`CharsMixin` — chain methods for character literals and ranges.

Validates user input, escapes regex metacharacters via
:func:`edify.compile.escape.escape_special`, and appends the resulting
character-shaped element to the top frame's children.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.protocol import BuilderProtocol
from edify.compile.escape import escape_special
from edify.elements.types.chars import (
    AnyOfCharsElement,
    AnythingButCharsElement,
    AnythingButRangeElement,
    AnythingButStringElement,
    CharElement,
    RangeElement,
    StringElement,
)
from edify.errors.input import (
    MustBeAStringError,
    MustBeOneCharacterError,
    MustBeSingleCharacterError,
    MustHaveASmallerValueError,
)


class CharsMixin(BuilderProtocol):
    """Provides chain methods for char/string literals, ranges, and char classes."""

    def string(self, value: str) -> Self:
        """Return a new builder with the literal ``value`` appended."""
        _ensure_is_string("Value", value)
        _ensure_non_empty("Value", value)
        escaped_value = escape_special(value)
        element = _string_or_char_element(escaped_value, source_length=len(value))
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def char(self, value: str) -> Self:
        """Return a new builder with the single-character literal ``value`` appended."""
        _ensure_is_string("Value", value)
        _ensure_single_character("Value", value)
        escaped_value = escape_special(value)
        element = CharElement(value=escaped_value)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def range(self, start_character: str, end_character: str) -> Self:
        """Return a new builder with a ``[start-end]`` range appended."""
        _ensure_single_character("a", start_character)
        _ensure_single_character("b", end_character)
        _ensure_ascending_codepoints(start_character, end_character)
        element = RangeElement(start=start_character, end=end_character)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def any_of_chars(self, characters: str) -> Self:
        """Return a new builder with an inline ``[characters]`` class appended."""
        escaped_characters = escape_special(characters)
        element = AnyOfCharsElement(value=escaped_characters)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def anything_but_string(self, value: str) -> Self:
        """Return a new builder with a per-character negation of ``value`` appended."""
        _ensure_is_string("Value", value)
        _ensure_non_empty("Value", value)
        escaped_value = escape_special(value)
        element = AnythingButStringElement(value=escaped_value)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def anything_but_chars(self, characters: str) -> Self:
        """Return a new builder with an inline ``[^characters]`` negation appended."""
        _ensure_is_string("Value", characters)
        _ensure_non_empty("Value", characters)
        escaped_characters = escape_special(characters)
        element = AnythingButCharsElement(value=escaped_characters)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)

    def anything_but_range(self, start_character: str, end_character: str) -> Self:
        """Return a new builder with a ``[^start-end]`` negated range appended."""
        _ensure_single_character("a", start_character)
        _ensure_single_character("b", end_character)
        _ensure_ascending_codepoints(start_character, end_character)
        element = AnythingButRangeElement(start=start_character, end=end_character)
        new_state = self._state.with_element_added_to_top(element)
        return self._with_state(new_state)


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


def _ensure_single_character(label: str, value: object) -> None:
    """Raise :class:`MustBeSingleCharacterError` when ``value`` is not a length-1 string."""
    if isinstance(value, str) and len(value) == 1:
        return
    actual_type_name = type(value).__name__
    raise MustBeSingleCharacterError(label, actual_type_name)


def _ensure_ascending_codepoints(first_character: str, second_character: str) -> None:
    """Raise :class:`MustHaveASmallerValueError` when ``first`` does not order before ``second``."""
    if ord(first_character) < ord(second_character):
        return
    raise MustHaveASmallerValueError(first_character, second_character)


def _string_or_char_element(escaped_value: str, source_length: int) -> CharElement | StringElement:
    """Pick :class:`CharElement` for single-character inputs, :class:`StringElement` otherwise."""
    if source_length == 1:
        return CharElement(value=escaped_value)
    return StringElement(value=escaped_value)
