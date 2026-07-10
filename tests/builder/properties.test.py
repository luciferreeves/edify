"""Property assertions — no chain ever silently drops or duplicates an element.

Every quantifier, group, capture, named capture, and subexpression in a
randomly-generated composition emits its own fragment exactly once and in
the correct place in the output regex string.
"""

from __future__ import annotations

from dataclasses import dataclass

from hypothesis import given
from hypothesis import strategies as st

from edify import Pattern, RegexBuilder


@dataclass(frozen=True)
class LeafNode:
    """A single element with an optional quantifier attached before it."""

    element_name: str
    element_args: tuple[int, ...]
    element_regex: str
    quantifier: tuple[str, tuple[int, ...], str] | None


@dataclass(frozen=True)
class GroupNode:
    """A non-capturing group wrapping ``children``."""

    children: tuple[object, ...]


@dataclass(frozen=True)
class CaptureNode:
    """An unnamed capture group wrapping ``children``."""

    children: tuple[object, ...]


@dataclass(frozen=True)
class NamedCaptureNode:
    """A named-capture group wrapping ``children``; the name is assigned deterministically."""

    children: tuple[object, ...]


@dataclass(frozen=True)
class SubexpressionNode:
    """A subexpression built as a separate ``Pattern`` and merged into the parent."""

    children: tuple[object, ...]


_QUANTIFIER_STRATEGIES: list[st.SearchStrategy[tuple[str, tuple[int, ...], str]]] = [
    st.just(("optional", (), "?")),
    st.just(("zero_or_more", (), "*")),
    st.just(("zero_or_more_lazy", (), "*?")),
    st.just(("one_or_more", (), "+")),
    st.just(("one_or_more_lazy", (), "+?")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("exactly", (n,), f"{{{n}}}")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("at_least", (n,), f"{{{n},}}")),
    st.integers(min_value=1, max_value=8).map(lambda n: ("at_most", (n,), f"{{0,{n}}}")),
    st.tuples(
        st.integers(min_value=0, max_value=6),
        st.integers(min_value=1, max_value=8),
    )
    .filter(lambda pair: pair[0] < pair[1])
    .map(lambda pair: ("between", pair, f"{{{pair[0]},{pair[1]}}}")),
    st.tuples(
        st.integers(min_value=0, max_value=6),
        st.integers(min_value=1, max_value=8),
    )
    .filter(lambda pair: pair[0] < pair[1])
    .map(lambda pair: ("between_lazy", pair, f"{{{pair[0]},{pair[1]}}}?")),
]

_ELEMENT_STRATEGIES = [
    st.just(("digit", (), "\\d")),
    st.just(("word", (), "\\w")),
    st.just(("whitespace_char", (), "\\s")),
    st.just(("letter", (), "[a-zA-Z]")),
    st.just(("uppercase", (), "[A-Z]")),
    st.just(("lowercase", (), "[a-z]")),
    st.just(("alphanumeric", (), "[a-zA-Z0-9]")),
]

_element_pick = st.one_of(*_ELEMENT_STRATEGIES)
_quantifier_pick_or_none = st.one_of(st.none(), *_QUANTIFIER_STRATEGIES)


_ElementCall = tuple[str, tuple[int, ...], str]
_QuantifierCall = tuple[str, tuple[int, ...], str]


def _build_leaf(pair: tuple[_ElementCall, _QuantifierCall | None]) -> LeafNode:
    element, quantifier = pair
    element_name, element_args, element_regex = element
    return LeafNode(
        element_name=element_name,
        element_args=element_args,
        element_regex=element_regex,
        quantifier=quantifier,
    )


_leaf_node_strategy = st.tuples(_element_pick, _quantifier_pick_or_none).map(_build_leaf)


def _extend(children_strategy: st.SearchStrategy) -> st.SearchStrategy:
    children_list = st.lists(children_strategy, min_size=1, max_size=4)
    group_nodes = children_list.map(lambda children: GroupNode(tuple(children)))
    capture_nodes = children_list.map(lambda children: CaptureNode(tuple(children)))
    named_capture_nodes = children_list.map(lambda children: NamedCaptureNode(tuple(children)))
    subexpression_nodes = children_list.map(lambda children: SubexpressionNode(tuple(children)))
    return st.one_of(group_nodes, capture_nodes, named_capture_nodes, subexpression_nodes)


_node_strategy = st.recursive(_leaf_node_strategy, _extend, max_leaves=6)


def _apply_sequence(
    builder,
    nodes: list[object],
    name_counter: int,
) -> tuple[object, str, int]:
    """Apply ``nodes`` to ``builder`` in order; return the updated triple."""
    fragments: list[str] = []
    for node in nodes:
        builder, fragment, name_counter = _apply_node(builder, node, name_counter)
        fragments.append(fragment)
    combined_regex = "".join(fragments)
    return builder, combined_regex, name_counter


def _apply_node(builder, node, name_counter: int) -> tuple[object, str, int]:
    """Dispatch on ``node`` type, applying it to ``builder`` and returning the fragment."""
    if isinstance(node, LeafNode):
        return _apply_leaf(builder, node, name_counter)
    if isinstance(node, GroupNode):
        return _apply_group(builder, node, name_counter)
    if isinstance(node, CaptureNode):
        return _apply_capture(builder, node, name_counter)
    if isinstance(node, NamedCaptureNode):
        return _apply_named_capture(builder, node, name_counter)
    return _apply_subexpression(builder, node, name_counter)


def _apply_leaf(builder, node: LeafNode, name_counter: int) -> tuple[object, str, int]:
    """Apply a single leaf element, optionally preceded by a quantifier."""
    if node.quantifier is None:
        builder_after_element = getattr(builder, node.element_name)(*node.element_args)
        return builder_after_element, node.element_regex, name_counter
    quantifier_name, quantifier_args, quantifier_suffix = node.quantifier
    builder_after_quantifier = getattr(builder, quantifier_name)(*quantifier_args)
    builder_after_element = getattr(builder_after_quantifier, node.element_name)(*node.element_args)
    fragment = f"{node.element_regex}{quantifier_suffix}"
    return builder_after_element, fragment, name_counter


def _apply_group(builder, node: GroupNode, name_counter: int) -> tuple[object, str, int]:
    """Apply a non-capturing group around ``node.children``."""
    builder_opened = builder.group()
    builder_inner, inner_regex, name_counter = _apply_sequence(
        builder_opened, list(node.children), name_counter
    )
    builder_closed = builder_inner.end()
    return builder_closed, f"(?:{inner_regex})", name_counter


def _apply_capture(builder, node: CaptureNode, name_counter: int) -> tuple[object, str, int]:
    """Apply an unnamed capture group around ``node.children``."""
    builder_opened = builder.capture()
    builder_inner, inner_regex, name_counter = _apply_sequence(
        builder_opened, list(node.children), name_counter
    )
    builder_closed = builder_inner.end()
    return builder_closed, f"({inner_regex})", name_counter


def _apply_named_capture(
    builder,
    node: NamedCaptureNode,
    name_counter: int,
) -> tuple[object, str, int]:
    """Apply a named-capture group with a deterministically-assigned name."""
    assigned_name = f"n{name_counter}"
    next_counter = name_counter + 1
    builder_opened = builder.named_capture(assigned_name)
    builder_inner, inner_regex, next_counter = _apply_sequence(
        builder_opened, list(node.children), next_counter
    )
    builder_closed = builder_inner.end()
    return builder_closed, f"(?P<{assigned_name}>{inner_regex})", next_counter


def _apply_subexpression(
    builder,
    node: SubexpressionNode,
    name_counter: int,
) -> tuple[object, str, int]:
    """Apply a subexpression built as an independent ``Pattern`` and merged in."""
    sub_pattern = Pattern()
    sub_pattern_finished, sub_regex, next_counter = _apply_sequence(
        sub_pattern, list(node.children), name_counter
    )
    builder_after_merge = builder.subexpression(sub_pattern_finished)
    return builder_after_merge, sub_regex, next_counter


@given(st.lists(_leaf_node_strategy, min_size=1, max_size=8))
def test_bare_element_chain_emits_the_concatenation_of_element_fragments(nodes):
    builder = RegexBuilder()
    builder_after, expected_regex, _ = _apply_sequence(builder, list(nodes), 0)
    assert builder_after.to_regex_string() == expected_regex


@given(st.lists(_leaf_node_strategy, min_size=1, max_size=8))
def test_every_quantifier_chain_call_produces_exactly_one_output_quantifier(nodes):
    builder = RegexBuilder()
    builder_after, expected_regex, _ = _apply_sequence(builder, list(nodes), 0)
    assert builder_after.to_regex_string() == expected_regex


@given(st.lists(_node_strategy, min_size=1, max_size=6))
def test_composition_over_groups_captures_and_subexpressions_is_faithful(nodes):
    builder = RegexBuilder()
    builder_after, expected_regex, _ = _apply_sequence(builder, list(nodes), 0)
    assert builder_after.to_regex_string() == expected_regex
