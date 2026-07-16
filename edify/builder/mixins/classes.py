"""The :class:`ClassesMixin` — chain methods for the built-in character classes.

Each method appends a single leaf element to the top frame's children. The
state helper takes care of applying any pending quantifier before the
element lands.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.leaves import (
    AlphanumericElement,
    AnyCharElement,
    CarriageReturnElement,
    DigitElement,
    LetterElement,
    LowercaseElement,
    NewLineElement,
    NonDigitElement,
    NonWhitespaceCharElement,
    NonWordBoundaryElement,
    NonWordElement,
    NullByteElement,
    TabElement,
    UppercaseElement,
    WhitespaceCharElement,
    WordBoundaryElement,
    WordElement,
)


class ClassesMixin(BuilderProtocol):
    """Provides chain methods that append a single built-in character class."""

    def any_char(self) -> Self:
        """Return a new builder with a ``.`` (any character) appended."""
        new_state = self.state.with_element_added_to_top(AnyCharElement())
        return self.with_state(new_state)

    def whitespace_char(self) -> Self:
        """Return a new builder with a ``\\s`` (whitespace) appended."""
        new_state = self.state.with_element_added_to_top(WhitespaceCharElement())
        return self.with_state(new_state)

    def non_whitespace_char(self) -> Self:
        """Return a new builder with a ``\\S`` (non-whitespace) appended."""
        new_state = self.state.with_element_added_to_top(NonWhitespaceCharElement())
        return self.with_state(new_state)

    def digit(self) -> Self:
        """Return a new builder with a ``\\d`` (digit) appended."""
        new_state = self.state.with_element_added_to_top(DigitElement())
        return self.with_state(new_state)

    def non_digit(self) -> Self:
        """Return a new builder with a ``\\D`` (non-digit) appended."""
        new_state = self.state.with_element_added_to_top(NonDigitElement())
        return self.with_state(new_state)

    def word(self) -> Self:
        """Return a new builder with a ``\\w`` (word character) appended."""
        new_state = self.state.with_element_added_to_top(WordElement())
        return self.with_state(new_state)

    def non_word(self) -> Self:
        """Return a new builder with a ``\\W`` (non-word character) appended."""
        new_state = self.state.with_element_added_to_top(NonWordElement())
        return self.with_state(new_state)

    def word_boundary(self) -> Self:
        """Return a new builder with a ``\\b`` (word boundary) appended."""
        new_state = self.state.with_element_added_to_top(WordBoundaryElement())
        return self.with_state(new_state)

    def non_word_boundary(self) -> Self:
        """Return a new builder with a ``\\B`` (non-word-boundary) appended."""
        new_state = self.state.with_element_added_to_top(NonWordBoundaryElement())
        return self.with_state(new_state)

    def new_line(self) -> Self:
        """Return a new builder with a ``\\n`` (line feed) appended."""
        new_state = self.state.with_element_added_to_top(NewLineElement())
        return self.with_state(new_state)

    def carriage_return(self) -> Self:
        """Return a new builder with a ``\\r`` (carriage return) appended."""
        new_state = self.state.with_element_added_to_top(CarriageReturnElement())
        return self.with_state(new_state)

    def tab(self) -> Self:
        """Return a new builder with a ``\\t`` (tab) appended."""
        new_state = self.state.with_element_added_to_top(TabElement())
        return self.with_state(new_state)

    def null_byte(self) -> Self:
        """Return a new builder with a ``\\0`` (null byte) appended."""
        new_state = self.state.with_element_added_to_top(NullByteElement())
        return self.with_state(new_state)

    def letter(self) -> Self:
        """Return a new builder with ``[a-zA-Z]`` (ASCII letter) appended."""
        new_state = self.state.with_element_added_to_top(LetterElement())
        return self.with_state(new_state)

    def uppercase(self) -> Self:
        """Return a new builder with ``[A-Z]`` (ASCII uppercase letter) appended."""
        new_state = self.state.with_element_added_to_top(UppercaseElement())
        return self.with_state(new_state)

    def lowercase(self) -> Self:
        """Return a new builder with ``[a-z]`` (ASCII lowercase letter) appended."""
        new_state = self.state.with_element_added_to_top(LowercaseElement())
        return self.with_state(new_state)

    def alphanumeric(self) -> Self:
        """Return a new builder with ``[a-zA-Z0-9]`` (ASCII alphanumeric) appended."""
        new_state = self.state.with_element_added_to_top(AlphanumericElement())
        return self.with_state(new_state)
