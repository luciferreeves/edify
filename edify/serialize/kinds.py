"""Registry mapping AST element classes to their public serialization ``kind`` strings.

The ``kind`` value is the sole public identifier of an element in the
canonical serialization. Internal class names (``ExactlyElement``) are never
part of the wire format — only the corresponding ``kind`` (``"exactly"``).
"""

from __future__ import annotations

from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.chars import (
    AnyOfCharsElement,
    AnythingButCharsElement,
    AnythingButRangeElement,
    AnythingButStringElement,
    CharElement,
    RangeElement,
    StringElement,
)
from edify.elements.types.groups import (
    AnyOfElement,
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
    GroupElement,
    SubexpressionElement,
)
from edify.elements.types.leaves import (
    AlphanumericElement,
    AnyCharElement,
    CarriageReturnElement,
    DigitElement,
    EndOfInputElement,
    LetterElement,
    LowercaseElement,
    NewLineElement,
    NonDigitElement,
    NonWhitespaceCharElement,
    NonWordBoundaryElement,
    NonWordElement,
    NoopElement,
    NullByteElement,
    StartOfInputElement,
    TabElement,
    UppercaseElement,
    WhitespaceCharElement,
    WordBoundaryElement,
    WordElement,
)
from edify.elements.types.quantifiers import (
    AtLeastElement,
    AtMostElement,
    BetweenElement,
    BetweenLazyElement,
    ExactlyElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    OptionalElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
)
from edify.elements.types.root import RootElement

_CLASS_BY_KIND = {
    "root": RootElement,
    "start": StartOfInputElement,
    "end": EndOfInputElement,
    "any": AnyCharElement,
    "whitespace": WhitespaceCharElement,
    "non-whitespace": NonWhitespaceCharElement,
    "digit": DigitElement,
    "non-digit": NonDigitElement,
    "word": WordElement,
    "non-word": NonWordElement,
    "word-boundary": WordBoundaryElement,
    "non-word-boundary": NonWordBoundaryElement,
    "newline": NewLineElement,
    "carriage-return": CarriageReturnElement,
    "tab": TabElement,
    "null-byte": NullByteElement,
    "letter": LetterElement,
    "upper": UppercaseElement,
    "lower": LowercaseElement,
    "alnum": AlphanumericElement,
    "noop": NoopElement,
    "char": CharElement,
    "string": StringElement,
    "range": RangeElement,
    "chars": AnyOfCharsElement,
    "non-chars": AnythingButCharsElement,
    "non-range": AnythingButRangeElement,
    "non-string": AnythingButStringElement,
    "capture": CaptureElement,
    "named-capture": NamedCaptureElement,
    "back-reference": BackReferenceElement,
    "named-back-reference": NamedBackReferenceElement,
    "group": GroupElement,
    "any-of": AnyOfElement,
    "subexpression": SubexpressionElement,
    "assert-ahead": AssertAheadElement,
    "assert-not-ahead": AssertNotAheadElement,
    "assert-behind": AssertBehindElement,
    "assert-not-behind": AssertNotBehindElement,
    "optional": OptionalElement,
    "zero-or-more": ZeroOrMoreElement,
    "zero-or-more-lazy": ZeroOrMoreLazyElement,
    "one-or-more": OneOrMoreElement,
    "one-or-more-lazy": OneOrMoreLazyElement,
    "exactly": ExactlyElement,
    "at-least": AtLeastElement,
    "at-most": AtMostElement,
    "between": BetweenElement,
    "between-lazy": BetweenLazyElement,
}

_KIND_BY_CLASS = {cls: kind for kind, cls in _CLASS_BY_KIND.items()}


def kind_for(element_class: type) -> str:
    """Return the public ``kind`` string registered for ``element_class``."""
    return _KIND_BY_CLASS[element_class]


def class_for(kind: str) -> type:
    """Return the element class registered under ``kind``."""
    return _CLASS_BY_KIND[kind]
