"""Leaf element classes — value-less nodes of the edify AST.

Each leaf represents a regex construct that emits a fixed string and carries
no parameters: ``\\d`` for :class:`DigitElement`, ``\\b`` for
:class:`WordBoundaryElement`, ``^`` for :class:`StartOfInputElement`, etc.

Every leaf is :func:`dataclasses.dataclass` with ``frozen=True`` so the whole
AST is immutable; the builder produces new branches by constructing new
elements rather than mutating existing ones. All leaves inherit from
:class:`edify.elements.types.base.BaseElement` so they participate in the
``Element`` union and in :func:`isinstance` dispatch.
"""

from __future__ import annotations

from dataclasses import dataclass

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class StartOfInputElement(BaseElement):
    """The ``^`` anchor."""


@dataclass(frozen=True)
class EndOfInputElement(BaseElement):
    """The ``$`` anchor."""


@dataclass(frozen=True)
class AnyCharElement(BaseElement):
    """The ``.`` wildcard, matching any single character."""


@dataclass(frozen=True)
class WhitespaceCharElement(BaseElement):
    """The ``\\s`` character class (whitespace)."""


@dataclass(frozen=True)
class NonWhitespaceCharElement(BaseElement):
    """The ``\\S`` character class (non-whitespace)."""


@dataclass(frozen=True)
class DigitElement(BaseElement):
    """The ``\\d`` character class (decimal digit)."""


@dataclass(frozen=True)
class NonDigitElement(BaseElement):
    """The ``\\D`` character class (non-digit)."""


@dataclass(frozen=True)
class WordElement(BaseElement):
    """The ``\\w`` character class (word character)."""


@dataclass(frozen=True)
class NonWordElement(BaseElement):
    """The ``\\W`` character class (non-word character)."""


@dataclass(frozen=True)
class WordBoundaryElement(BaseElement):
    """The ``\\b`` zero-width assertion at a word boundary."""


@dataclass(frozen=True)
class NonWordBoundaryElement(BaseElement):
    """The ``\\B`` zero-width assertion off a word boundary."""


@dataclass(frozen=True)
class NewLineElement(BaseElement):
    """The ``\\n`` line-feed character."""


@dataclass(frozen=True)
class CarriageReturnElement(BaseElement):
    """The ``\\r`` carriage-return character."""


@dataclass(frozen=True)
class TabElement(BaseElement):
    """The ``\\t`` horizontal-tab character."""


@dataclass(frozen=True)
class NullByteElement(BaseElement):
    """The ``\\0`` null byte."""


@dataclass(frozen=True)
class LetterElement(BaseElement):
    """The ``[a-zA-Z]`` ASCII letter character class."""


@dataclass(frozen=True)
class UppercaseElement(BaseElement):
    """The ``[A-Z]`` ASCII uppercase-letter character class."""


@dataclass(frozen=True)
class LowercaseElement(BaseElement):
    """The ``[a-z]`` ASCII lowercase-letter character class."""


@dataclass(frozen=True)
class AlphanumericElement(BaseElement):
    """The ``[a-zA-Z0-9]`` ASCII alphanumeric character class."""


@dataclass(frozen=True)
class NoopElement(BaseElement):
    """A no-op marker that emits an empty string in the compile path."""
