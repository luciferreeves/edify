"""Annotated re.VERBOSE-compatible rendering of edify AST elements."""

from __future__ import annotations

from edify.compile.dispatch import render_element
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

_INDENT_STEP = "  "
_COMMENT_COLUMN = 24


def verbose_elements(elements: tuple[BaseElement, ...]) -> str:
    """Return the pattern as an annotated ``re.VERBOSE``-compatible multi-line string."""
    lines: list[str] = []
    for element in elements:
        lines.extend(_verbose(element, depth=0))
    return "\n".join(lines)


def _verbose(element: BaseElement, depth: int) -> list[str]:
    """Return the ``re.VERBOSE`` lines for a single ``element`` at nesting ``depth``."""
    prefix = _INDENT_STEP * depth
    leaf_line = _leaf_line(element)
    if leaf_line is not None:
        fragment, comment = leaf_line
        return [_render_line(prefix, fragment, comment)]
    char_line = _char_line(element)
    if char_line is not None:
        fragment, comment = char_line
        return [_render_line(prefix, fragment, comment)]
    quantifier_lines = _quantifier_lines(element, depth)
    if quantifier_lines is not None:
        return quantifier_lines
    group_lines = _group_lines(element, depth)
    if group_lines is not None:
        return group_lines
    capture_lines = _capture_lines(element, depth)
    if capture_lines is not None:
        return capture_lines
    assertion_lines = _assertion_lines(element, depth)
    if assertion_lines is not None:
        return assertion_lines
    fragment = render_element(element)
    return [_render_line(prefix, fragment, f"unrecognized ({type(element).__name__})")]


def _leaf_line(element: BaseElement) -> tuple[str, str] | None:
    """Return the ``(fragment, comment)`` pair for a leaf element, or ``None``."""
    if isinstance(element, StartOfInputElement):
        return ("^", "start of input")
    if isinstance(element, EndOfInputElement):
        return ("$", "end of input")
    if isinstance(element, AnyCharElement):
        return (".", "any single character")
    if isinstance(element, WhitespaceCharElement):
        return ("\\s", "any whitespace character")
    if isinstance(element, NonWhitespaceCharElement):
        return ("\\S", "any non-whitespace character")
    if isinstance(element, DigitElement):
        return ("\\d", "any digit (0-9)")
    if isinstance(element, NonDigitElement):
        return ("\\D", "any non-digit")
    if isinstance(element, WordElement):
        return ("\\w", "any word character")
    if isinstance(element, NonWordElement):
        return ("\\W", "any non-word character")
    if isinstance(element, WordBoundaryElement):
        return ("\\b", "word boundary")
    if isinstance(element, NonWordBoundaryElement):
        return ("\\B", "non-word boundary")
    if isinstance(element, NewLineElement):
        return ("\\n", "line feed")
    if isinstance(element, CarriageReturnElement):
        return ("\\r", "carriage return")
    if isinstance(element, TabElement):
        return ("\\t", "tab")
    if isinstance(element, NullByteElement):
        return ("\\0", "null byte")
    if isinstance(element, LetterElement):
        return ("[a-zA-Z]", "any ASCII letter")
    if isinstance(element, UppercaseElement):
        return ("[A-Z]", "any ASCII uppercase letter")
    if isinstance(element, LowercaseElement):
        return ("[a-z]", "any ASCII lowercase letter")
    if isinstance(element, AlphanumericElement):
        return ("[a-zA-Z0-9]", "any ASCII letter or digit")
    if isinstance(element, NoopElement):
        return ("", "no-op")
    return None


def _char_line(element: BaseElement) -> tuple[str, str] | None:
    """Return the ``(fragment, comment)`` pair for a character-shaped element, or ``None``."""
    if isinstance(element, CharElement):
        return (element.value, f'literal "{element.value}"')
    if isinstance(element, StringElement):
        return (element.value, f'literal string "{element.value}"')
    if isinstance(element, RangeElement):
        return (f"[{element.start}-{element.end}]", f"range {element.start}-{element.end}")
    if isinstance(element, AnyOfCharsElement):
        return (f"[{element.value}]", f"one of {element.value!r}")
    if isinstance(element, AnythingButCharsElement):
        return (f"[^{element.value}]", f"none of {element.value!r}")
    if isinstance(element, AnythingButRangeElement):
        return (
            f"[^{element.start}-{element.end}]",
            f"none of range {element.start}-{element.end}",
        )
    if isinstance(element, AnythingButStringElement):
        fragment = render_element(element)
        return (fragment, f"per-position negation of {element.value!r}")
    return None


def _quantifier_lines(element: BaseElement, depth: int) -> list[str] | None:
    """Return the ``re.VERBOSE`` lines for a quantifier element, or ``None``."""
    prefix = _INDENT_STEP * depth
    if isinstance(element, OptionalElement):
        return _wrap_child(prefix, element.child, "?", "optional (zero or one)", depth)
    if isinstance(element, ZeroOrMoreElement):
        return _wrap_child(prefix, element.child, "*", "zero or more (greedy)", depth)
    if isinstance(element, ZeroOrMoreLazyElement):
        return _wrap_child(prefix, element.child, "*?", "zero or more (lazy)", depth)
    if isinstance(element, OneOrMoreElement):
        return _wrap_child(prefix, element.child, "+", "one or more (greedy)", depth)
    if isinstance(element, OneOrMoreLazyElement):
        return _wrap_child(prefix, element.child, "+?", "one or more (lazy)", depth)
    if isinstance(element, ExactlyElement):
        return _wrap_child(
            prefix, element.child, f"{{{element.times}}}", f"exactly {element.times}", depth
        )
    if isinstance(element, AtLeastElement):
        return _wrap_child(
            prefix, element.child, f"{{{element.times},}}", f"at least {element.times}", depth
        )
    if isinstance(element, AtMostElement):
        return _wrap_child(
            prefix, element.child, f"{{0,{element.times}}}", f"at most {element.times}", depth
        )
    if isinstance(element, BetweenElement):
        suffix = f"{{{element.lower},{element.upper}}}"
        return _wrap_child(
            prefix,
            element.child,
            suffix,
            f"between {element.lower} and {element.upper} (greedy)",
            depth,
        )
    if isinstance(element, BetweenLazyElement):
        suffix = f"{{{element.lower},{element.upper}}}?"
        return _wrap_child(
            prefix,
            element.child,
            suffix,
            f"between {element.lower} and {element.upper} (lazy)",
            depth,
        )
    return None


def _wrap_child(
    prefix: str,
    child: BaseElement,
    suffix: str,
    comment: str,
    depth: int,
) -> list[str]:
    """Return the child's lines with ``suffix`` and ``comment`` attached to the emitted regex."""
    child_lines = _verbose(child, depth)
    if len(child_lines) == 1:
        raw_child_source = _extract_source(child_lines[0])
        combined_fragment = f"{raw_child_source}{suffix}"
        if _needs_group(child):
            combined_fragment = f"(?:{raw_child_source}){suffix}"
        return [_render_line(prefix, combined_fragment, comment)]
    return [
        _render_line(prefix, "(?:", f"begin group for {comment}"),
        *child_lines,
        _render_line(prefix, f"){suffix}", f"end group; apply {comment}"),
    ]


def _group_lines(element: BaseElement, depth: int) -> list[str] | None:
    """Return the ``re.VERBOSE`` lines for a group / alternation / subexpression, or ``None``."""
    prefix = _INDENT_STEP * depth
    if isinstance(element, GroupElement):
        return [
            _render_line(prefix, "(?:", "begin non-capturing group"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end non-capturing group"),
        ]
    if isinstance(element, AnyOfElement):
        return _alternation_lines(prefix, element, depth)
    if isinstance(element, SubexpressionElement):
        return _render_children(element.children, depth)
    return None


def _alternation_lines(prefix: str, element: AnyOfElement, depth: int) -> list[str]:
    """Return the ``(?: a | b | c )`` layout for :class:`AnyOfElement`."""
    if not element.children:
        return [_render_line(prefix, "(?:)", "empty alternation")]
    lines: list[str] = [_render_line(prefix, "(?:", "begin alternation")]
    inner_depth = depth + 1
    for index, child in enumerate(element.children):
        alternative_prefix = _INDENT_STEP * inner_depth
        lines.append(_render_line(alternative_prefix, "", f"alternative {index + 1}"))
        lines.extend(_verbose(child, inner_depth))
        if index < len(element.children) - 1:
            lines.append(_render_line(alternative_prefix, "|", "or"))
    lines.append(_render_line(prefix, ")", "end alternation"))
    return lines


def _capture_lines(element: BaseElement, depth: int) -> list[str] | None:
    """Return the ``re.VERBOSE`` lines for a capture element, or ``None``."""
    prefix = _INDENT_STEP * depth
    if isinstance(element, CaptureElement):
        return [
            _render_line(prefix, "(", "begin captured group"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end captured group"),
        ]
    if isinstance(element, NamedCaptureElement):
        return [
            _render_line(prefix, f"(?P<{element.name}>", f'begin group named "{element.name}"'),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", f'end group named "{element.name}"'),
        ]
    if isinstance(element, BackReferenceElement):
        return [
            _render_line(prefix, f"\\{element.index}", f"back-reference to group {element.index}")
        ]
    if isinstance(element, NamedBackReferenceElement):
        return [
            _render_line(
                prefix,
                f"(?P={element.name})",
                f'back-reference to group "{element.name}"',
            )
        ]
    return None


def _assertion_lines(element: BaseElement, depth: int) -> list[str] | None:
    """Return the ``re.VERBOSE`` lines for a lookaround assertion element, or ``None``."""
    prefix = _INDENT_STEP * depth
    if isinstance(element, AssertAheadElement):
        return [
            _render_line(prefix, "(?=", "begin positive lookahead"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end positive lookahead"),
        ]
    if isinstance(element, AssertNotAheadElement):
        return [
            _render_line(prefix, "(?!", "begin negative lookahead"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end negative lookahead"),
        ]
    if isinstance(element, AssertBehindElement):
        return [
            _render_line(prefix, "(?<=", "begin positive lookbehind"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end positive lookbehind"),
        ]
    if isinstance(element, AssertNotBehindElement):
        return [
            _render_line(prefix, "(?<!", "begin negative lookbehind"),
            *_render_children(element.children, depth + 1),
            _render_line(prefix, ")", "end negative lookbehind"),
        ]
    return None


def _render_children(children: tuple[BaseElement, ...], depth: int) -> list[str]:
    """Return the ``re.VERBOSE`` lines for a sequence of children at ``depth``."""
    lines: list[str] = []
    for child in children:
        lines.extend(_verbose(child, depth))
    return lines


def _render_line(prefix: str, fragment: str, comment: str) -> str:
    """Return one aligned output line: ``<prefix><fragment>   # <comment>``."""
    left = f"{prefix}{fragment}"
    padding_needed = _COMMENT_COLUMN - len(left)
    if padding_needed < 2:
        padding_needed = 2
    padding = " " * padding_needed
    return f"{left}{padding}# {comment}"


def _extract_source(rendered_line: str) -> str:
    """Return the raw regex fragment from an already-rendered ``_render_line`` output."""
    without_comment = rendered_line.split("#", 1)[0]
    return without_comment.rstrip().lstrip()


def _needs_group(child: BaseElement) -> bool:
    """Return True when ``child``'s regex fragment needs grouping to apply a quantifier."""
    if isinstance(child, StringElement):
        return len(child.value) > 1
    return False
