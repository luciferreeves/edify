"""ASCII railroad-diagram renderer for edify AST elements."""

from __future__ import annotations

import re

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
from edify.introspect.types import Diagram

_EDGE = "-->"
_EDGE_WIDTH = len(_EDGE)
_INDENT = 3


def render_ascii(elements: tuple[BaseElement, ...]) -> str:
    """Return an ASCII railroad diagram for ``elements`` as a multi-line string."""
    start_box = _boxed("START")
    end_box = _boxed("END")
    element_diagrams = [_element_diagram(element) for element in elements]
    parts: list[Diagram] = [start_box, *element_diagrams, end_box]
    diagram = _join_horizontal(parts)
    indented = _indent_left(diagram, _INDENT)
    return "\n".join(indented.rows)


def _boxed(label: str) -> Diagram:
    """Return a three-row boxed diagram with ``label`` centered in a one-space margin."""
    content = f" {label} "
    border = "+" + "-" * len(content) + "+"
    middle = "|" + content + "|"
    return Diagram(rows=(border, middle, border), entry_row=1, width=len(border))


def _element_diagram(element: BaseElement) -> Diagram:
    """Return the diagram for a single AST ``element``."""
    inline = _inline_label(element)
    if inline is not None:
        return _boxed(inline)
    quantifier = _quantifier_diagram(element)
    if quantifier is not None:
        return quantifier
    if isinstance(element, AnyOfElement):
        return _alternation_diagram(element.children)
    if isinstance(element, SubexpressionElement):
        return _sequence_diagram(element.children)
    if isinstance(element, GroupElement):
        return _annotated_sequence(element.children, "grouped")
    if isinstance(element, CaptureElement):
        return _annotated_sequence(element.children, "captured")
    if isinstance(element, NamedCaptureElement):
        return _annotated_sequence(element.children, f'saved as "{element.name}"')
    if isinstance(element, BackReferenceElement):
        return _boxed(f"match same text as group {element.index}")
    if isinstance(element, NamedBackReferenceElement):
        return _boxed(f'match same text as "{element.name}"')
    if isinstance(element, AssertAheadElement):
        return _annotated_sequence(element.children, "must be followed by")
    if isinstance(element, AssertNotAheadElement):
        return _annotated_sequence(element.children, "must NOT be followed by")
    if isinstance(element, AssertBehindElement):
        return _annotated_sequence(element.children, "must be preceded by")
    if isinstance(element, AssertNotBehindElement):
        return _annotated_sequence(element.children, "must NOT be preceded by")
    return _boxed(f"?{type(element).__name__}")


def _inline_label(element: BaseElement) -> str | None:
    """Return a short plain-English label for a leaf or character element, or ``None``."""
    leaf = leaf_label(element)
    if leaf is not None:
        return leaf
    return char_label(element)


def leaf_label(element: BaseElement) -> str | None:
    """Return the plain-English label for a leaf element, or ``None``."""
    if isinstance(element, StartOfInputElement):
        return "text starts here"
    if isinstance(element, EndOfInputElement):
        return "text ends here"
    if isinstance(element, AnyCharElement):
        return "any character"
    if isinstance(element, WhitespaceCharElement):
        return "whitespace"
    if isinstance(element, NonWhitespaceCharElement):
        return "non-whitespace"
    if isinstance(element, DigitElement):
        return "digit"
    if isinstance(element, NonDigitElement):
        return "non-digit character"
    if isinstance(element, WordElement):
        return "word character"
    if isinstance(element, NonWordElement):
        return "non-word character"
    if isinstance(element, WordBoundaryElement):
        return "word boundary"
    if isinstance(element, NonWordBoundaryElement):
        return "non-word boundary"
    if isinstance(element, NewLineElement):
        return "newline"
    if isinstance(element, CarriageReturnElement):
        return "carriage return"
    if isinstance(element, TabElement):
        return "tab"
    if isinstance(element, NullByteElement):
        return "null byte"
    if isinstance(element, LetterElement):
        return "letter"
    if isinstance(element, UppercaseElement):
        return "uppercase letter"
    if isinstance(element, LowercaseElement):
        return "lowercase letter"
    if isinstance(element, AlphanumericElement):
        return "letter or digit"
    if isinstance(element, NoopElement):
        return "no-op"
    return None


def char_label(element: BaseElement) -> str | None:
    """Return the plain-English label for a character-shaped element, or ``None``."""
    if isinstance(element, CharElement):
        return f'"{_display_string(element.value)}"'
    if isinstance(element, StringElement):
        return f'"{_display_string(element.value)}"'
    if isinstance(element, RangeElement):
        return f'any character from "{element.start}" to "{element.end}"'
    if isinstance(element, AnyOfCharsElement):
        return f'any of "{_display_string(element.value)}"'
    if isinstance(element, AnythingButCharsElement):
        return f'anything except "{_display_string(element.value)}"'
    if isinstance(element, AnythingButRangeElement):
        return f'anything outside "{element.start}"-"{element.end}"'
    if isinstance(element, AnythingButStringElement):
        return f'anything except the string "{_display_string(element.value)}"'
    return None


def _display_string(value: str) -> str:
    """Return ``value`` with regex-escape backslashes stripped for human display."""
    return re.sub(r"\\(.)", r"\1", value)


def _quantifier_diagram(element: BaseElement) -> Diagram | None:
    """Return the diagram for a quantifier wrapping a child, or ``None`` when not a quantifier."""
    label = _quantifier_label(element)
    if label is None:
        return None
    return _boxed(label)


def _quantifier_label(element: BaseElement) -> str | None:
    """Return a single-line plain-English label for a quantifier, or ``None``."""
    if isinstance(element, ExactlyElement):
        return _phrase_count(element.times, element.child)
    if isinstance(element, OneOrMoreElement):
        return f"one or more {_child_plural(element.child)}"
    if isinstance(element, OneOrMoreLazyElement):
        return f"one or more {_child_plural(element.child)} (lazy)"
    if isinstance(element, ZeroOrMoreElement):
        return f"zero or more {_child_plural(element.child)}"
    if isinstance(element, ZeroOrMoreLazyElement):
        return f"zero or more {_child_plural(element.child)} (lazy)"
    if isinstance(element, OptionalElement):
        return f"optional {_child_singular(element.child)}"
    if isinstance(element, AtLeastElement):
        return f"at least {element.times} {_child_plural(element.child)}"
    if isinstance(element, AtMostElement):
        return f"at most {element.times} {_child_plural(element.child)}"
    if isinstance(element, BetweenElement):
        return f"{element.lower} to {element.upper} {_child_plural(element.child)}"
    if isinstance(element, BetweenLazyElement):
        return f"{element.lower} to {element.upper} {_child_plural(element.child)} (lazy)"
    return None


def _child_singular(child: BaseElement) -> str:
    """Return the singular plain-English label for a quantifier's child."""
    label = _inline_label(child)
    if label is not None:
        return label
    return "group"


def _child_plural(child: BaseElement) -> str:
    """Return the plural plain-English label for a quantifier's child."""
    return _pluralize(_child_singular(child))


def _phrase_count(times: int, child: BaseElement) -> str:
    """Return a ``"{times} {label}"`` phrase, pluralized when ``times`` is not one."""
    label = _child_singular(child)
    if times == 1:
        return f"1 {label}"
    return f"{times} {_pluralize(label)}"


def _pluralize(label: str) -> str:
    """Return an English plural of ``label`` (respecting literal-string quotes)."""
    if label.startswith('"') and label.endswith('"'):
        return label
    if len(label) >= 2 and label.endswith("y") and label[-2] not in "aeiou":
        return label[:-1] + "ies"
    return label + "s"


def _sequence_diagram(children: tuple[BaseElement, ...]) -> Diagram:
    """Return the horizontal join of ``children`` diagrams with edge connectors."""
    if not children:
        return _boxed("nothing")
    diagrams = [_element_diagram(child) for child in children]
    return _join_horizontal(diagrams)


def _annotated_sequence(children: tuple[BaseElement, ...], annotation: str) -> Diagram:
    """Return the diagram for ``children`` with ``annotation`` displayed under the middle."""
    inner = _sequence_diagram(children)
    caption = f"({annotation})"
    return _caption_below(inner, caption)


def _caption_below(diagram: Diagram, caption: str) -> Diagram:
    """Return ``diagram`` with a caption row appended below and centered under it.

    When ``caption`` is longer than ``diagram.width``, the diagram is widened; the
    entry row is padded with dashes so the horizontal flow line continues to the
    new right edge, and the caption is centered under the widened diagram.
    """
    new_width = max(diagram.width, len(caption))
    extra = new_width - diagram.width
    padded_rows: list[str] = []
    for row_index, row in enumerate(diagram.rows):
        if extra == 0:
            padded_rows.append(row)
        elif row_index == diagram.entry_row:
            padded_rows.append(row + "-" * extra)
        else:
            padded_rows.append(row + " " * extra)
    left_pad = (new_width - len(caption)) // 2
    right_pad = new_width - left_pad - len(caption)
    caption_row = " " * left_pad + caption + " " * right_pad
    return Diagram(
        rows=(*padded_rows, caption_row),
        entry_row=diagram.entry_row,
        width=new_width,
    )


def _alternation_diagram(children: tuple[BaseElement, ...]) -> Diagram:
    """Return a vertical fork/merge diagram over ``children`` alternatives."""
    if not children:
        return _boxed("nothing")
    branches = [_element_diagram(child) for child in children]
    branch_widths = [branch.width for branch in branches]
    branch_width = max(branch_widths)
    padded = [_widen(branch, branch_width) for branch in branches]
    branch_entry_rows: list[int] = []
    body_rows: list[str] = []
    for index, branch in enumerate(padded):
        base_row = len(body_rows)
        for row_index, row in enumerate(branch.rows):
            if row_index == branch.entry_row:
                body_rows.append(f"+--->{row}----+")
            else:
                body_rows.append(f"|    {row}    |")
        branch_entry_rows.append(base_row + branch.entry_row)
        if index < len(padded) - 1:
            body_rows.append(f"|    {' ' * branch_width}    |")
    body_rows = _clip_trunk_above(body_rows, branch_entry_rows[0])
    body_rows = _clip_trunk_below(body_rows, branch_entry_rows[-1])
    entry_row = branch_entry_rows[len(branch_entry_rows) // 2]
    return Diagram(
        rows=tuple(body_rows),
        entry_row=entry_row,
        width=branch_width + 10,
    )


def _clip_trunk_above(rows: list[str], first_entry: int) -> list[str]:
    """Replace trunk ``|`` characters in rows above ``first_entry`` with spaces."""
    result = list(rows)
    for index in range(first_entry):
        row = result[index]
        result[index] = " " + row[1:-1] + " "
    return result


def _clip_trunk_below(rows: list[str], last_entry: int) -> list[str]:
    """Replace trunk ``|`` characters in rows below ``last_entry`` with spaces."""
    result = list(rows)
    for index in range(last_entry + 1, len(result)):
        row = result[index]
        result[index] = " " + row[1:-1] + " "
    return result


def _pad_right(diagram: Diagram, target_width: int) -> Diagram:
    """Return ``diagram`` right-padded with spaces so every row reaches ``target_width``."""
    extra = target_width - diagram.width
    padded_rows_list = [row + " " * extra for row in diagram.rows]
    new_rows = tuple(padded_rows_list)
    return Diagram(rows=new_rows, entry_row=diagram.entry_row, width=target_width)


def _widen(diagram: Diagram, target_width: int) -> Diagram:
    """Return ``diagram`` widened to ``target_width``, extending single-box borders in place."""
    if diagram.width >= target_width:
        return diagram
    if _looks_like_single_box(diagram):
        return _widen_box(diagram, target_width)
    return _pad_right(diagram, target_width)


def _looks_like_single_box(diagram: Diagram) -> bool:
    """Return ``True`` when ``diagram`` is a plain three-row ``+---+ | X | +---+`` box."""
    if len(diagram.rows) != 3 or diagram.entry_row != 1:
        return False
    top, _middle, bottom = diagram.rows
    return top == bottom and set(top[1:-1]) == {"-"}


def _widen_box(diagram: Diagram, target_width: int) -> Diagram:
    """Return a simple box ``diagram`` widened to ``target_width`` by extending its borders."""
    extra = target_width - diagram.width
    _top, middle, _bottom = diagram.rows
    new_border = "+" + "-" * (target_width - 2) + "+"
    interior = middle[1:-1]
    new_middle = "|" + interior + " " * extra + "|"
    return Diagram(
        rows=(new_border, new_middle, new_border),
        entry_row=1,
        width=target_width,
    )


def _join_horizontal(diagrams: list[Diagram]) -> Diagram:
    """Return the horizontal concatenation of ``diagrams`` with edge connectors between."""
    result = diagrams[0]
    for next_diagram in diagrams[1:]:
        result = _join_two(result, next_diagram)
    return result


def _join_two(left: Diagram, right: Diagram) -> Diagram:
    """Return ``left`` and ``right`` joined on their shared entry row with an ``_EDGE`` between."""
    target_entry = max(left.entry_row, right.entry_row)
    left_shifted = _align_entry_row(left, target_entry)
    right_shifted = _align_entry_row(right, target_entry)
    height = max(len(left_shifted.rows), len(right_shifted.rows))
    left_expanded = _pad_below(left_shifted, height)
    right_expanded = _pad_below(right_shifted, height)
    new_rows: list[str] = []
    for row_index in range(height):
        connector = _EDGE if row_index == target_entry else " " * _EDGE_WIDTH
        new_rows.append(left_expanded.rows[row_index] + connector + right_expanded.rows[row_index])
    combined_width = left_expanded.width + _EDGE_WIDTH + right_expanded.width
    return Diagram(rows=tuple(new_rows), entry_row=target_entry, width=combined_width)


def _align_entry_row(diagram: Diagram, target_entry_row: int) -> Diagram:
    """Return ``diagram`` with blank rows above so its entry row lands at ``target_entry_row``."""
    if diagram.entry_row >= target_entry_row:
        return diagram
    extra_rows_above = target_entry_row - diagram.entry_row
    blank = " " * diagram.width
    new_rows = (blank,) * extra_rows_above + diagram.rows
    return Diagram(rows=new_rows, entry_row=target_entry_row, width=diagram.width)


def _pad_below(diagram: Diagram, target_height: int) -> Diagram:
    """Return ``diagram`` with blank rows appended so it reaches ``target_height`` rows total."""
    current_height = len(diagram.rows)
    if current_height >= target_height:
        return diagram
    extra_rows_below = target_height - current_height
    blank = " " * diagram.width
    new_rows = diagram.rows + (blank,) * extra_rows_below
    return Diagram(rows=new_rows, entry_row=diagram.entry_row, width=diagram.width)


def _indent_left(diagram: Diagram, spaces: int) -> Diagram:
    """Return ``diagram`` with ``spaces`` blank columns prepended to every row."""
    prefix = " " * spaces
    indented_rows_list = [prefix + row for row in diagram.rows]
    new_rows = tuple(indented_rows_list)
    return Diagram(
        rows=new_rows,
        entry_row=diagram.entry_row,
        width=diagram.width + spaces,
    )
