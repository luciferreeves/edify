"""Plain-English explanation renderer for edify AST elements."""

from __future__ import annotations

from edify.elements.types.base import BaseElement
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


def explain_elements(elements: tuple[BaseElement, ...]) -> str:
    """Return a bullet-list explanation plus accept examples for ``elements``."""
    if not elements:
        return "This pattern is empty and matches an empty string."
    flat_elements = _flatten(elements)
    build_lines = _build_lines(flat_elements)
    all_match_examples = _generate_match_examples(flat_elements)
    non_empty_match_examples = [example for example in all_match_examples if example]
    lines: list[str] = [f"- {description}" for description in build_lines]
    if non_empty_match_examples:
        lines.append("")
        lines.append("Text this pattern accepts:")
        lines.extend(f"    {example}" for example in non_empty_match_examples)
    return "\n".join(lines)


def _flatten(elements: tuple[BaseElement, ...]) -> tuple[BaseElement, ...]:
    """Return ``elements`` with every :class:`SubexpressionElement` recursively inlined."""
    result: list[BaseElement] = []
    for element in elements:
        if isinstance(element, SubexpressionElement):
            result.extend(_flatten(element.children))
        else:
            result.append(element)
    return tuple(result)


def _build_lines(elements: tuple[BaseElement, ...]) -> list[str]:
    """Return one bullet description per top-level element after skipping the anchor pair."""
    working = list(elements)
    starts_with_start_anchor = bool(working) and isinstance(working[0], StartOfInputElement)
    if starts_with_start_anchor:
        working = working[1:]
    if (
        len(working) >= 2
        and isinstance(working[-1], EndOfInputElement)
        and isinstance(working[-2], AssertAheadElement)
    ):
        trailing_lookahead = working[-2]
        working = working[:-2]
        trailing_line = (
            f"The text must end at {_describe_inline_children(trailing_lookahead.children)}."
        )
    elif working and isinstance(working[-1], EndOfInputElement):
        working = working[:-1]
        trailing_line = None
    else:
        trailing_line = None
    lines: list[str] = []
    for index, element in enumerate(working):
        is_first = index == 0
        lines.append(
            _describe_step(
                element,
                is_first_step=is_first,
                anchored_at_start=starts_with_start_anchor,
            )
        )
    if trailing_line is not None:
        lines.append(trailing_line)
    return lines


def _wrap_step(step_number: int, description: str) -> str:
    """Return the description prefixed with the step number and indented continuation."""
    prefix = f"  {step_number}. "
    continuation_prefix = " " * len(prefix)
    words = description.split()
    if not words:
        return prefix.rstrip()
    lines: list[str] = []
    current_line = prefix + words[0]
    max_width = 76
    for word in words[1:]:
        candidate = current_line + " " + word
        if len(candidate) > max_width:
            lines.append(current_line)
            current_line = continuation_prefix + word
        else:
            current_line = candidate
    lines.append(current_line)
    return "\n".join(lines)


def _describe_step(
    element: BaseElement,
    *,
    is_first_step: bool,
    anchored_at_start: bool,
) -> str:
    """Return a one-sentence plain-English description of a top-level ``element``."""
    if isinstance(element, WordBoundaryElement):
        return (
            "This point must fall on a word boundary — where a letter, digit, "
            "or underscore meets something else."
        )
    if isinstance(element, NonWordBoundaryElement):
        return (
            "This point must NOT fall on a word boundary — it must be inside a "
            "run of letters, digits, or underscores, or between two other "
            "characters."
        )
    starting_form = "The text must start with" if anchored_at_start else "The text must contain"
    connector = starting_form if is_first_step else "Then the text must have"
    if isinstance(element, OptionalElement):
        return f"Optional: {_describe_optional_inner(element.child)}."
    if isinstance(element, ZeroOrMoreElement):
        return f"{connector} zero or more {_describe_plural(element.child)}."
    if isinstance(element, ZeroOrMoreLazyElement):
        return f"{connector} zero or more {_describe_plural(element.child)} (as few as possible)."
    if isinstance(element, OneOrMoreElement):
        return f"{connector} one or more {_describe_plural(element.child)}."
    if isinstance(element, OneOrMoreLazyElement):
        return f"{connector} one or more {_describe_plural(element.child)} (as few as possible)."
    if isinstance(element, ExactlyElement):
        return f"{connector} exactly {element.times} {_describe_plural(element.child)}."
    if isinstance(element, AtLeastElement):
        return f"{connector} at least {element.times} {_describe_plural(element.child)}."
    if isinstance(element, AtMostElement):
        return f"{connector} at most {element.times} {_describe_plural(element.child)}."
    if isinstance(element, BetweenElement):
        return (
            f"{connector} between {element.lower} and {element.upper} "
            f"{_describe_plural(element.child)}."
        )
    if isinstance(element, BetweenLazyElement):
        return (
            f"{connector} between {element.lower} and {element.upper} "
            f"{_describe_plural(element.child)} (as few as possible)."
        )
    if isinstance(element, CaptureElement):
        return f"{connector} {_describe_inline_children(element.children)}."
    if isinstance(element, NamedCaptureElement):
        return f"{connector} {_describe_inline_children(element.children)}."
    if isinstance(element, BackReferenceElement):
        return f"{connector} the exact same text that appeared earlier in group #{element.index}."
    if isinstance(element, NamedBackReferenceElement):
        return (
            f"{connector} the exact same text that appeared earlier in the "
            f'group labeled "{element.name}".'
        )
    if isinstance(element, AssertAheadElement):
        return f"Then the text must be followed by {_describe_inline_children(element.children)}."
    if isinstance(element, AssertNotAheadElement):
        return (
            f"Then the text must NOT be followed by {_describe_inline_children(element.children)}."
        )
    if isinstance(element, AssertBehindElement):
        return (
            f"Just before this point, {_describe_inline_children(element.children)} "
            "must have appeared."
        )
    if isinstance(element, AssertNotBehindElement):
        return (
            f"Just before this point, {_describe_inline_children(element.children)} "
            "must NOT have appeared."
        )
    if isinstance(element, GroupElement):
        return f"{connector} {_describe_inline_children(element.children)}."
    if isinstance(element, AnyOfElement):
        return f"{connector} {_describe_alternatives(element.children)}."
    inline = _describe_inline(element)
    return f"{connector} {inline}."


def _describe_optional_inner(element: BaseElement) -> str:
    """Return the phrase used after "may optionally continue with"."""
    if isinstance(element, SubexpressionElement | GroupElement):
        return _describe_inline_children(element.children)
    if isinstance(element, CharElement):
        return f'"{_unescape_literal(element.value)}"'
    if isinstance(element, StringElement):
        return f'"{_unescape_literal(element.value)}"'
    return _describe_inline(element)


def _describe_plural(element: BaseElement) -> str:
    """Return the plural-stem phrase for ``element`` used after a count word like "one or more"."""
    if isinstance(element, AnyCharElement):
        return "characters (any character)"
    if isinstance(element, WhitespaceCharElement):
        return "whitespace characters (space, tab, newline, etc.)"
    if isinstance(element, NonWhitespaceCharElement):
        return "non-whitespace characters"
    if isinstance(element, DigitElement):
        return "digits (0-9)"
    if isinstance(element, NonDigitElement):
        return "non-digit characters"
    if isinstance(element, WordElement):
        return "letters, digits, or underscores"
    if isinstance(element, NonWordElement):
        return "characters that are not letters, digits, or underscores"
    if isinstance(element, NewLineElement):
        return 'line-feed characters ("\\n")'
    if isinstance(element, CarriageReturnElement):
        return 'carriage-return characters ("\\r")'
    if isinstance(element, TabElement):
        return 'tab characters ("\\t")'
    if isinstance(element, NullByteElement):
        return 'null bytes ("\\0")'
    if isinstance(element, LetterElement):
        return "letters (a-z or A-Z)"
    if isinstance(element, UppercaseElement):
        return "uppercase letters (A-Z)"
    if isinstance(element, LowercaseElement):
        return "lowercase letters (a-z)"
    if isinstance(element, AlphanumericElement):
        return "letters or digits (a-z, A-Z, or 0-9)"
    if isinstance(element, CharElement):
        return f'copies of the character "{_unescape_literal(element.value)}"'
    if isinstance(element, StringElement):
        return f'copies of the text "{_unescape_literal(element.value)}"'
    if isinstance(element, RangeElement):
        return f'characters from "{element.start}" through "{element.end}"'
    if isinstance(element, AnyOfCharsElement):
        return f'characters from the set "{element.value}"'
    if isinstance(element, AnythingButCharsElement):
        return f'characters NOT from the set "{element.value}"'
    if isinstance(element, AnythingButRangeElement):
        return f'characters outside "{element.start}" through "{element.end}"'
    return f"of {_describe_inline(element)}"


def _describe_inline(element: BaseElement) -> str:
    """Return an inline phrase for ``element`` suitable for embedding in a sentence."""
    if isinstance(element, StartOfInputElement):
        return "the very beginning of the text"
    if isinstance(element, EndOfInputElement):
        return "the very end of the text"
    if isinstance(element, AnyCharElement):
        return "any single character"
    if isinstance(element, WhitespaceCharElement):
        return "one whitespace character (space, tab, newline, etc.)"
    if isinstance(element, NonWhitespaceCharElement):
        return "one non-whitespace character"
    if isinstance(element, DigitElement):
        return "one digit (0-9)"
    if isinstance(element, NonDigitElement):
        return "one non-digit character"
    if isinstance(element, WordElement):
        return "one letter, digit, or underscore"
    if isinstance(element, NonWordElement):
        return "one character that is not a letter, digit, or underscore"
    if isinstance(element, WordBoundaryElement):
        return "a word boundary"
    if isinstance(element, NonWordBoundaryElement):
        return "a non-word-boundary position"
    if isinstance(element, NewLineElement):
        return 'a line-feed character (the newline "\\n")'
    if isinstance(element, CarriageReturnElement):
        return 'a carriage-return character ("\\r")'
    if isinstance(element, TabElement):
        return 'a tab character ("\\t")'
    if isinstance(element, NullByteElement):
        return 'the null byte ("\\0")'
    if isinstance(element, LetterElement):
        return "one letter (a-z or A-Z)"
    if isinstance(element, UppercaseElement):
        return "one uppercase letter (A-Z)"
    if isinstance(element, LowercaseElement):
        return "one lowercase letter (a-z)"
    if isinstance(element, AlphanumericElement):
        return "one letter or digit (a-z, A-Z, or 0-9)"
    if isinstance(element, NoopElement):
        return "nothing"
    if isinstance(element, CharElement):
        return f'"{_unescape_literal(element.value)}"'
    if isinstance(element, StringElement):
        return f'"{_unescape_literal(element.value)}"'
    if isinstance(element, RangeElement):
        return f'one character from "{element.start}" through "{element.end}"'
    if isinstance(element, AnyOfCharsElement):
        return f'one character from the set "{element.value}"'
    if isinstance(element, AnythingButCharsElement):
        return f'one character NOT from the set "{element.value}"'
    if isinstance(element, AnythingButRangeElement):
        return f'one character outside "{element.start}" through "{element.end}"'
    if isinstance(element, AnythingButStringElement):
        return (
            f"a run of {len(element.value)} characters "
            f'not matching "{element.value}" position-for-position'
        )
    if isinstance(element, OptionalElement):
        return f"an optional {_describe_optional_inner(element.child)}"
    if isinstance(element, ZeroOrMoreElement):
        return f"zero or more {_describe_plural(element.child)}"
    if isinstance(element, ZeroOrMoreLazyElement):
        return f"zero or more {_describe_plural(element.child)} (as few as possible)"
    if isinstance(element, OneOrMoreElement):
        return f"one or more {_describe_plural(element.child)}"
    if isinstance(element, OneOrMoreLazyElement):
        return f"one or more {_describe_plural(element.child)} (as few as possible)"
    if isinstance(element, ExactlyElement):
        return f"exactly {element.times} {_describe_plural(element.child)}"
    if isinstance(element, AtLeastElement):
        return f"at least {element.times} {_describe_plural(element.child)}"
    if isinstance(element, AtMostElement):
        return f"at most {element.times} {_describe_plural(element.child)}"
    if isinstance(element, BetweenElement):
        return f"between {element.lower} and {element.upper} {_describe_plural(element.child)}"
    if isinstance(element, BetweenLazyElement):
        return (
            f"between {element.lower} and {element.upper} "
            f"{_describe_plural(element.child)} (as few as possible)"
        )
    if isinstance(element, CaptureElement):
        return f"{_describe_inline_children(element.children)} (captured)"
    if isinstance(element, NamedCaptureElement):
        return (
            f"{_describe_inline_children(element.children)} "
            f'(captured under the label "{element.name}")'
        )
    if isinstance(element, GroupElement):
        return _describe_inline_children(element.children)
    if isinstance(element, AnyOfElement):
        return _describe_alternatives(element.children)
    if isinstance(element, SubexpressionElement):
        return _describe_inline_children(element.children)
    if isinstance(element, BackReferenceElement):
        return f"the same text that group #{element.index} captured"
    if isinstance(element, NamedBackReferenceElement):
        return f'the same text that the "{element.name}" group captured'
    return type(element).__name__


def _describe_inline_children(children: tuple[BaseElement, ...]) -> str:
    """Return the "A, then B, then C" phrase describing ``children`` in sequence."""
    flat = _flatten(children)
    if not flat:
        return "nothing"
    phrases = [_describe_inline(child) for child in flat]
    if len(phrases) == 1:
        return phrases[0]
    return ", then ".join(phrases)


def _describe_alternatives(children: tuple[BaseElement, ...]) -> str:
    """Return the "either A or B or C" phrase describing an alternation."""
    if not children:
        return "nothing"
    phrases = [_describe_inline(child) for child in children]
    if len(phrases) == 1:
        return phrases[0]
    if len(phrases) == 2:
        return f"either {phrases[0]} or {phrases[1]}"
    joined = ", ".join(phrases[:-1])
    return f"either {joined}, or {phrases[-1]}"


def _generate_match_examples(elements: tuple[BaseElement, ...]) -> list[str]:
    """Return a small set of concrete strings that the pattern matches."""
    seeds = [_build_example(elements, alternative_index) for alternative_index in range(3)]
    unique_seeds: list[str] = []
    for seed in seeds:
        if seed not in unique_seeds:
            unique_seeds.append(seed)
    return unique_seeds


def _build_example(elements: tuple[BaseElement, ...], alternative_index: int) -> str:
    """Return one matching example string using ``alternative_index`` where alternation applies."""
    parts = [_example_for(element, alternative_index) for element in elements]
    return "".join(parts)


_LETTER_ROTATION = ("e", "o", "a", "i", "u")
_DIGIT_ROTATION = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
_UPPERCASE_ROTATION = ("A", "B", "C", "D", "E")
_ALPHANUMERIC_ROTATION = ("a", "1", "b", "2", "c", "3")
_WORD_ROTATION = ("a", "b", "1", "_", "c", "2", "d")


def _example_for(element: BaseElement, alternative_index: int) -> str:
    """Return a piece of text ``element`` accepts, using ``alternative_index`` where relevant."""
    if isinstance(
        element,
        StartOfInputElement | EndOfInputElement | WordBoundaryElement | NonWordBoundaryElement,
    ):
        return ""
    if isinstance(element, AnyCharElement):
        return _LETTER_ROTATION[alternative_index % len(_LETTER_ROTATION)]
    if isinstance(element, WhitespaceCharElement):
        return " "
    if isinstance(element, NonWhitespaceCharElement):
        return _LETTER_ROTATION[alternative_index % len(_LETTER_ROTATION)]
    if isinstance(element, DigitElement):
        return _DIGIT_ROTATION[alternative_index % len(_DIGIT_ROTATION)]
    if isinstance(element, NonDigitElement):
        return _LETTER_ROTATION[alternative_index % len(_LETTER_ROTATION)]
    if isinstance(element, WordElement):
        return _WORD_ROTATION[alternative_index % len(_WORD_ROTATION)]
    if isinstance(element, NonWordElement):
        return "-"
    if isinstance(element, NewLineElement):
        return "\n"
    if isinstance(element, CarriageReturnElement):
        return "\r"
    if isinstance(element, TabElement):
        return "\t"
    if isinstance(element, NullByteElement):
        return "\0"
    if isinstance(element, LetterElement):
        return _LETTER_ROTATION[alternative_index % len(_LETTER_ROTATION)]
    if isinstance(element, UppercaseElement):
        return _UPPERCASE_ROTATION[alternative_index % len(_UPPERCASE_ROTATION)]
    if isinstance(element, LowercaseElement):
        return _LETTER_ROTATION[alternative_index % len(_LETTER_ROTATION)]
    if isinstance(element, AlphanumericElement):
        return _ALPHANUMERIC_ROTATION[alternative_index % len(_ALPHANUMERIC_ROTATION)]
    if isinstance(element, NoopElement):
        return ""
    if isinstance(element, CharElement):
        return _unescape_literal(element.value)
    if isinstance(element, StringElement):
        return _unescape_literal(element.value)
    if isinstance(element, RangeElement):
        return element.start
    if isinstance(element, AnyOfCharsElement):
        if not element.value:
            return "a"
        raw = _unescape_literal(element.value)
        return raw[alternative_index % len(raw)]
    if isinstance(element, AnythingButCharsElement):
        return _pick_character_not_in(element.value)
    if isinstance(element, AnythingButRangeElement):
        return _pick_character_outside_range(element.start, element.end)
    if isinstance(element, AnythingButStringElement):
        return "x" * len(element.value) if element.value else ""
    if isinstance(element, OptionalElement):
        if alternative_index % 2 == 0:
            return _example_for(element.child, alternative_index)
        return ""
    if isinstance(element, ZeroOrMoreElement | ZeroOrMoreLazyElement):
        return _expand_variable(element.child, alternative_index, minimum=1)
    if isinstance(element, OneOrMoreElement | OneOrMoreLazyElement):
        return _expand_variable(element.child, alternative_index, minimum=1)
    if isinstance(element, ExactlyElement):
        return _expand_child_n_times(element.child, alternative_index, element.times)
    if isinstance(element, AtLeastElement):
        return _expand_child_n_times(element.child, alternative_index, element.times + 1)
    if isinstance(element, AtMostElement):
        take = max(1, min(element.times, 2 + alternative_index % max(1, element.times)))
        return _expand_child_n_times(element.child, alternative_index, take)
    if isinstance(element, BetweenElement | BetweenLazyElement):
        take = element.lower + alternative_index % max(1, element.upper - element.lower + 1)
        take = max(element.lower, min(element.upper, take))
        return _expand_child_n_times(element.child, alternative_index, take)
    if isinstance(
        element, CaptureElement | NamedCaptureElement | GroupElement | SubexpressionElement
    ):
        return "".join(_example_for(child, alternative_index) for child in element.children)
    if isinstance(element, AnyOfElement):
        if not element.children:
            return ""
        chosen = element.children[alternative_index % len(element.children)]
        return _example_for(chosen, alternative_index)
    if isinstance(element, AssertAheadElement | AssertBehindElement):
        return "".join(_example_for(child, alternative_index) for child in element.children)
    if isinstance(element, AssertNotAheadElement | AssertNotBehindElement):
        return ""
    if isinstance(element, BackReferenceElement | NamedBackReferenceElement):
        return "a"
    return ""


def _expand_variable(child: BaseElement, alternative_index: int, minimum: int) -> str:
    """Return a run of ``child`` examples between 3 and 6 characters long depending on rotation."""
    run_length = max(minimum, 3 + alternative_index % 3)
    return _expand_child_n_times(child, alternative_index, run_length)


def _expand_child_n_times(child: BaseElement, alternative_index: int, count: int) -> str:
    """Return ``count`` example pieces of ``child`` back-to-back, varying content per position."""
    pieces = [_example_for(child, alternative_index + position) for position in range(count)]
    return "".join(pieces)


def _unescape_literal(escaped_value: str) -> str:
    """Return ``escaped_value`` stripped of the leading backslashes edify adds around metachars."""
    result: list[str] = []
    index = 0
    while index < len(escaped_value):
        character = escaped_value[index]
        if character == "\\" and index + 1 < len(escaped_value):
            result.append(escaped_value[index + 1])
            index = index + 2
        else:
            result.append(character)
            index = index + 1
    return "".join(result)


def _pick_character_not_in(disallowed: str) -> str:
    """Return a single character that is not in ``disallowed``."""
    for candidate in "abcdefghijklmnopqrstuvwxyz0123456789":
        if candidate not in disallowed:
            return candidate
    return "!"


def _pick_character_outside_range(start: str, end: str) -> str:
    """Return a single character outside the ``start``-through-``end`` range."""
    for candidate in "abcdefghijklmnopqrstuvwxyz0123456789":
        if not (start <= candidate <= end):
            return candidate
    return "!"
