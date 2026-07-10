"""The sealed :data:`Element` union — every concrete element class spelled out."""

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

LeafElement = (
    StartOfInputElement
    | EndOfInputElement
    | AnyCharElement
    | WhitespaceCharElement
    | NonWhitespaceCharElement
    | DigitElement
    | NonDigitElement
    | WordElement
    | NonWordElement
    | WordBoundaryElement
    | NonWordBoundaryElement
    | NewLineElement
    | CarriageReturnElement
    | TabElement
    | NullByteElement
    | LetterElement
    | UppercaseElement
    | LowercaseElement
    | AlphanumericElement
    | NoopElement
)

CharShapedElement = (
    CharElement
    | StringElement
    | RangeElement
    | AnyOfCharsElement
    | AnythingButCharsElement
    | AnythingButRangeElement
    | AnythingButStringElement
)

CaptureGroupElement = (
    CaptureElement | NamedCaptureElement | BackReferenceElement | NamedBackReferenceElement
)

GroupingElement = (
    GroupElement
    | AnyOfElement
    | SubexpressionElement
    | AssertAheadElement
    | AssertNotAheadElement
    | AssertBehindElement
    | AssertNotBehindElement
)

QuantifierElement = (
    OptionalElement
    | ZeroOrMoreElement
    | ZeroOrMoreLazyElement
    | OneOrMoreElement
    | OneOrMoreLazyElement
    | ExactlyElement
    | AtLeastElement
    | AtMostElement
    | BetweenElement
    | BetweenLazyElement
)

Element = (
    StartOfInputElement
    | EndOfInputElement
    | AnyCharElement
    | WhitespaceCharElement
    | NonWhitespaceCharElement
    | DigitElement
    | NonDigitElement
    | WordElement
    | NonWordElement
    | WordBoundaryElement
    | NonWordBoundaryElement
    | NewLineElement
    | CarriageReturnElement
    | TabElement
    | NullByteElement
    | LetterElement
    | UppercaseElement
    | LowercaseElement
    | AlphanumericElement
    | NoopElement
    | CharElement
    | StringElement
    | RangeElement
    | AnyOfCharsElement
    | AnythingButCharsElement
    | AnythingButRangeElement
    | AnythingButStringElement
    | CaptureElement
    | NamedCaptureElement
    | BackReferenceElement
    | NamedBackReferenceElement
    | GroupElement
    | AnyOfElement
    | SubexpressionElement
    | AssertAheadElement
    | AssertNotAheadElement
    | AssertBehindElement
    | AssertNotBehindElement
    | QuantifierElement
    | RootElement
)
