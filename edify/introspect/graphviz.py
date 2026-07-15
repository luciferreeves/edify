"""Graphviz DOT / SVG renderer for edify AST elements."""

from __future__ import annotations

from edify.elements.types.base import BaseElement
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
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
from edify.elements.types.union import QuantifierElement
from edify.errors.introspect import MissingGraphvizDependencyError
from edify.introspect.ascii import _char_label, _leaf_label
from edify.introspect.types import Emission

try:
    import graphviz as _graphviz_module
except ImportError:
    _graphviz_module = None


def render_graphviz_svg(elements: tuple[BaseElement, ...]) -> str:
    """Return an SVG rendering of ``elements`` produced by Graphviz."""
    if _graphviz_module is None:
        raise MissingGraphvizDependencyError()
    dot_source = render_dot(elements)
    source = _graphviz_module.Source(dot_source, format="svg")
    piped_bytes: bytes = source.pipe(format="svg")
    return piped_bytes.decode("utf-8")


def render_dot(elements: tuple[BaseElement, ...]) -> str:
    """Return the DOT source describing ``elements``."""
    counter = _Counter()
    entry_id, exit_id, sequence_lines = _emit_sequence(elements, counter)
    body: list[str] = list(sequence_lines)
    if entry_id is None:
        body.append("    start -> end;")
    else:
        body.append(f"    start -> {entry_id};")
        body.append(f"    {exit_id} -> end;")
    header = [
        "digraph edify_pattern {",
        "    rankdir=LR;",
        '    node [shape=box, style=rounded, fontname="Menlo"];',
        '    edge [fontname="Menlo"];',
        '    start [label="START", shape=circle];',
        '    end   [label="END",   shape=circle];',
    ]
    return "\n".join(header + body + ["}"])


def _emit_sequence(
    elements: tuple[BaseElement, ...], counter: _Counter
) -> tuple[str | None, str | None, list[str]]:
    """Return ``(entry_id, exit_id, lines)`` for a left-to-right sequence of ``elements``."""
    if not elements:
        return None, None, []
    lines: list[str] = []
    first_entry: str | None = None
    prev_exit: str | None = None
    for element in elements:
        emission = _emit_element(element, counter)
        lines.extend(emission.lines)
        if first_entry is None:
            first_entry = emission.entry_id
        if prev_exit is not None:
            lines.append(f"    {prev_exit} -> {emission.entry_id};")
        prev_exit = emission.exit_id
    return first_entry, prev_exit, lines


def _emit_element(element: BaseElement, counter: _Counter) -> Emission:
    """Return the DOT emission for a single AST ``element``."""
    inline_label = _inline_label(element)
    if inline_label is not None:
        return _emit_leaf(inline_label, counter)
    if isinstance(element, AnyOfElement):
        return _emit_alternation(element.children, counter)
    if isinstance(element, SubexpressionElement):
        return _emit_subexpression(element.children, counter)
    if isinstance(element, GroupElement):
        return _emit_cluster(element.children, "grouped", counter)
    if isinstance(element, CaptureElement):
        return _emit_cluster(element.children, "captured", counter)
    if isinstance(element, NamedCaptureElement):
        return _emit_cluster(element.children, f'saved as "{element.name}"', counter)
    if isinstance(element, AssertAheadElement):
        return _emit_cluster(element.children, "must be followed by", counter)
    if isinstance(element, AssertNotAheadElement):
        return _emit_cluster(element.children, "must NOT be followed by", counter)
    if isinstance(element, AssertBehindElement):
        return _emit_cluster(element.children, "must be preceded by", counter)
    if isinstance(element, AssertNotBehindElement):
        return _emit_cluster(element.children, "must NOT be preceded by", counter)
    if isinstance(element, BackReferenceElement):
        return _emit_leaf(f"match same text as group {element.index}", counter)
    if isinstance(element, NamedBackReferenceElement):
        return _emit_leaf(f'match same text as "{element.name}"', counter)
    complex_quantifier = _emit_quantifier_cluster(element, counter)
    if complex_quantifier is not None:
        return complex_quantifier
    return _emit_leaf(f"?{type(element).__name__}", counter)


def _emit_leaf(label: str, counter: _Counter) -> Emission:
    """Emit a single box node labelled with ``label`` and return its emission."""
    node_id = counter.next("n")
    lines = (f'    {node_id} [label="{_escape_dot(label)}"];',)
    return Emission(entry_id=node_id, exit_id=node_id, lines=lines)


def _emit_alternation(children: tuple[BaseElement, ...], counter: _Counter) -> Emission:
    """Emit an alternation as fork/merge over ``children`` using junction points."""
    if not children:
        return _emit_leaf("nothing", counter)
    fork_id = counter.next("fork")
    merge_id = counter.next("merge")
    lines: list[str] = [
        f'    {fork_id} [label="", shape=point, width=0.08];',
        f'    {merge_id} [label="", shape=point, width=0.08];',
    ]
    for child in children:
        emission = _emit_element(child, counter)
        lines.extend(emission.lines)
        lines.append(f"    {fork_id} -> {emission.entry_id};")
        lines.append(f"    {emission.exit_id} -> {merge_id};")
    lines_tuple = tuple(lines)
    return Emission(entry_id=fork_id, exit_id=merge_id, lines=lines_tuple)


def _emit_subexpression(children: tuple[BaseElement, ...], counter: _Counter) -> Emission:
    """Emit a transparent subexpression as a plain sequence of ``children``."""
    if not children:
        return _emit_leaf("empty subexpression", counter)
    entry_id, exit_id, lines = _emit_sequence(children, counter)
    lines_tuple = tuple(lines)
    return Emission(entry_id=entry_id or "", exit_id=exit_id or "", lines=lines_tuple)


def _emit_cluster(
    children: tuple[BaseElement, ...], cluster_label: str, counter: _Counter
) -> Emission:
    """Emit ``children`` inside a dashed rounded cluster labelled ``cluster_label``."""
    if not children:
        return _emit_leaf(f"{cluster_label} (empty)", counter)
    cluster_id = counter.next("cluster")
    entry_id, exit_id, inner_lines = _emit_sequence(children, counter)
    lines: list[str] = [
        f"    subgraph cluster_{cluster_id} {{",
        f'        label="{_escape_dot(cluster_label)}";',
        '        style="dashed,rounded";',
        '        fontname="Menlo";',
    ]
    indented_inner_lines = [f"    {line}" for line in inner_lines]
    lines.extend(indented_inner_lines)
    lines.append("    }")
    lines_tuple = tuple(lines)
    return Emission(entry_id=entry_id or "", exit_id=exit_id or "", lines=lines_tuple)


def _emit_quantifier_cluster(element: BaseElement, counter: _Counter) -> Emission | None:
    """Emit a quantifier wrapping a complex child as a dashed cluster; ``None`` if not one."""
    quantifier_phrase = _quantifier_phrase(element)
    if quantifier_phrase is None:
        return None
    assert isinstance(element, QuantifierElement)
    child_emission = _emit_element(element.child, counter)
    cluster_id = counter.next("cluster")
    lines: list[str] = [
        f"    subgraph cluster_{cluster_id} {{",
        f'        label="{_escape_dot(quantifier_phrase)}";',
        '        style="dashed,rounded";',
        '        fontname="Menlo";',
    ]
    indented_child_lines = [f"    {line}" for line in child_emission.lines]
    lines.extend(indented_child_lines)
    lines.append("    }")
    lines_tuple = tuple(lines)
    return Emission(
        entry_id=child_emission.entry_id,
        exit_id=child_emission.exit_id,
        lines=lines_tuple,
    )


def _inline_label(element: BaseElement) -> str | None:
    """Return a single-line label for a leaf / char / simple-quantifier element, else ``None``."""
    leaf = _leaf_label(element)
    if leaf is not None:
        return leaf
    char = _char_label(element)
    if char is not None:
        return char
    return _simple_quantifier_label(element)


def _simple_quantifier_label(element: BaseElement) -> str | None:
    """Return a folded two-line label when a quantifier wraps a leaf / char element."""
    quantifier_phrase = _quantifier_phrase(element)
    if quantifier_phrase is None:
        return None
    assert isinstance(element, QuantifierElement)
    child = element.child
    child_label = _leaf_label(child) or _char_label(child)
    if child_label is None:
        return None
    return f"{child_label}\\n({quantifier_phrase})"


def _quantifier_phrase(element: BaseElement) -> str | None:
    """Return the plain-English quantifier phrase (e.g. ``"one or more"``) or ``None``."""
    if isinstance(element, ExactlyElement):
        return f"exactly {element.times}"
    if isinstance(element, OneOrMoreElement):
        return "one or more"
    if isinstance(element, OneOrMoreLazyElement):
        return "one or more (lazy)"
    if isinstance(element, ZeroOrMoreElement):
        return "zero or more"
    if isinstance(element, ZeroOrMoreLazyElement):
        return "zero or more (lazy)"
    if isinstance(element, OptionalElement):
        return "optional"
    if isinstance(element, AtLeastElement):
        return f"at least {element.times}"
    if isinstance(element, AtMostElement):
        return f"at most {element.times}"
    if isinstance(element, BetweenElement):
        return f"{element.lower} to {element.upper}"
    if isinstance(element, BetweenLazyElement):
        return f"{element.lower} to {element.upper} (lazy)"
    return None


def _escape_dot(label: str) -> str:
    """Return ``label`` with characters that break DOT double-quoted strings escaped."""
    backslash_escaped = label.replace("\\", "\\\\")
    quote_escaped = backslash_escaped.replace('"', '\\"')
    return quote_escaped.replace("\\\\n", "\\n")


class _Counter:
    """Monotonically increasing counter used to mint unique DOT node identifiers."""

    def __init__(self) -> None:
        self._value = 0

    def next(self, prefix: str) -> str:
        """Return the next ``prefix_<n>`` identifier and advance the counter."""
        self._value = self._value + 1
        return f"{prefix}_{self._value}"
