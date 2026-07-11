"""Tests for the Graphviz DOT / SVG renderer in :mod:`edify.introspect.graphviz`."""

import builtins
import importlib
import sys

import pytest

from edify import RegexBuilder
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.chars import (
    CharElement,
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
    DigitElement,
    EndOfInputElement,
    StartOfInputElement,
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
from edify.errors.introspect import MissingGraphvizDependencyError
from edify.introspect import graphviz as graphviz_module
from edify.introspect.graphviz import (
    _Counter,
    _escape_dot,
    render_dot,
    render_graphviz_svg,
)


def _dot(*elements) -> str:
    return render_dot(tuple(elements))


def test_empty_pattern_produces_direct_start_to_end_edge():
    output = _dot()
    assert "start -> end;" in output
    assert "digraph edify_pattern" in output


def test_single_digit_pattern_creates_one_labeled_node():
    output = _dot(DigitElement())
    assert 'label="digit"' in output
    assert "start -> n_1" in output
    assert "n_1 -> end" in output


def test_header_configures_left_to_right_layout_and_menlo_font():
    output = _dot(DigitElement())
    assert "rankdir=LR" in output
    assert 'fontname="Menlo"' in output


def test_start_and_end_terminals_are_circles():
    output = _dot(DigitElement())
    assert 'start [label="START", shape=circle]' in output
    assert 'end   [label="END",   shape=circle]' in output


def test_one_or_more_digit_folds_quantifier_as_second_line():
    output = _dot(OneOrMoreElement(child=DigitElement()))
    assert 'label="digit\\n(one or more)"' in output


def test_one_or_more_lazy_appends_lazy_marker_to_phrase():
    output = _dot(OneOrMoreLazyElement(child=DigitElement()))
    assert "one or more (lazy)" in output


def test_zero_or_more_reads_as_zero_or_more_phrase():
    output = _dot(ZeroOrMoreElement(child=DigitElement()))
    assert "zero or more" in output


def test_zero_or_more_lazy_appends_lazy_marker():
    output = _dot(ZeroOrMoreLazyElement(child=DigitElement()))
    assert "zero or more (lazy)" in output


def test_optional_reads_as_optional_phrase():
    output = _dot(OptionalElement(child=DigitElement()))
    assert "optional" in output


def test_exactly_reads_as_exactly_n_phrase():
    output = _dot(ExactlyElement(times=4, child=DigitElement()))
    assert "exactly 4" in output


def test_at_least_reads_as_at_least_n_phrase():
    output = _dot(AtLeastElement(times=3, child=DigitElement()))
    assert "at least 3" in output


def test_at_most_reads_as_at_most_n_phrase():
    output = _dot(AtMostElement(times=5, child=DigitElement()))
    assert "at most 5" in output


def test_between_reads_as_lower_to_upper_phrase():
    output = _dot(BetweenElement(lower=2, upper=5, child=DigitElement()))
    assert "2 to 5" in output


def test_between_lazy_appends_lazy_marker():
    output = _dot(BetweenLazyElement(lower=2, upper=5, child=DigitElement()))
    assert "2 to 5 (lazy)" in output


def test_alternation_creates_fork_and_merge_junction_points():
    output = _dot(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    assert "shape=point, width=0.08" in output
    assert output.count("shape=point") == 2
    assert output.count("fork_") >= 1
    assert output.count("merge_") >= 1


def test_alternation_emits_edge_from_fork_and_to_merge_for_each_branch():
    output = _dot(
        AnyOfElement(
            children=(
                StringElement(value="cat"),
                StringElement(value="dog"),
                StringElement(value="fish"),
            )
        )
    )
    assert output.count("fork_1 ->") == 3
    assert output.count("-> merge_2") == 3


def test_empty_alternation_becomes_nothing_placeholder():
    output = _dot(AnyOfElement(children=()))
    assert 'label="nothing"' in output


def test_named_capture_wraps_children_in_dashed_cluster():
    output = _dot(
        NamedCaptureElement(
            name="year",
            children=(ExactlyElement(times=4, child=DigitElement()),),
        )
    )
    assert 'label="saved as \\"year\\""' in output
    assert 'style="dashed,rounded"' in output
    assert "subgraph cluster_" in output


def test_unnamed_capture_wraps_children_in_captured_cluster():
    output = _dot(CaptureElement(children=(DigitElement(),)))
    assert 'label="captured"' in output


def test_empty_capture_becomes_captured_empty_placeholder():
    output = _dot(CaptureElement(children=()))
    assert "captured (empty)" in output


def test_group_wraps_children_in_grouped_cluster():
    output = _dot(GroupElement(children=(DigitElement(),)))
    assert 'label="grouped"' in output


def test_subexpression_flattens_into_a_plain_sequence():
    output = _dot(SubexpressionElement(children=(DigitElement(), WordElement())))
    assert "cluster_" not in output
    assert 'label="digit"' in output
    assert 'label="word character"' in output


def test_empty_subexpression_becomes_empty_placeholder():
    output = _dot(SubexpressionElement(children=()))
    assert "empty subexpression" in output


def test_start_of_input_reads_as_text_starts_here():
    output = _dot(StartOfInputElement())
    assert 'label="text starts here"' in output


def test_end_of_input_reads_as_text_ends_here():
    output = _dot(EndOfInputElement())
    assert 'label="text ends here"' in output


def test_backreference_reads_as_match_same_text_as_group_n():
    output = _dot(BackReferenceElement(index=2))
    assert "match same text as group 2" in output


def test_named_backreference_reads_as_match_same_text_as_name():
    output = _dot(NamedBackReferenceElement(name="year"))
    assert 'match same text as \\"year\\"' in output


def test_assert_ahead_wraps_children_in_must_be_followed_by_cluster():
    output = _dot(AssertAheadElement(children=(DigitElement(),)))
    assert '"must be followed by"' in output


def test_assert_not_ahead_wraps_children_in_must_not_be_followed_by_cluster():
    output = _dot(AssertNotAheadElement(children=(DigitElement(),)))
    assert "must NOT be followed by" in output


def test_assert_behind_wraps_children_in_must_be_preceded_by_cluster():
    output = _dot(AssertBehindElement(children=(DigitElement(),)))
    assert "must be preceded by" in output


def test_assert_not_behind_wraps_children_in_must_not_be_preceded_by_cluster():
    output = _dot(AssertNotBehindElement(children=(DigitElement(),)))
    assert "must NOT be preceded by" in output


def test_character_literal_display_strips_regex_escaping():
    output = _dot(CharElement(value="\\-"))
    assert '"\\"-\\""' in output


def test_quantifier_wrapping_complex_child_uses_cluster_not_inline_label():
    inner = AnyOfElement(children=(StringElement(value="a"), StringElement(value="b")))
    output = _dot(OneOrMoreElement(child=inner))
    assert '"one or more"' in output
    assert "subgraph cluster_" in output


def test_unknown_element_type_produces_question_mark_label():
    class MysteryElement(DigitElement.__mro__[1]):
        pass

    output = _dot(MysteryElement())
    assert "?MysteryElement" in output


def test_counter_advances_and_produces_unique_ids():
    counter = _Counter()
    first = counter.next("n")
    second = counter.next("n")
    third = counter.next("fork")
    assert first == "n_1"
    assert second == "n_2"
    assert third == "fork_3"


def test_escape_dot_escapes_backslashes_and_quotes():
    assert _escape_dot('a"b') == 'a\\"b'
    assert _escape_dot("a\\b") == "a\\\\b"


def test_escape_dot_preserves_newline_escape_for_two_line_labels():
    assert _escape_dot("digit\\n(one or more)") == "digit\\n(one or more)"


def test_render_dot_end_to_end_via_builder():
    dot = RegexBuilder().any_of("cat", "dog", "fish").to_regex()
    output = render_dot(dot.elements)
    assert 'label="\\"cat\\""' in output
    assert 'label="\\"dog\\""' in output
    assert 'label="\\"fish\\""' in output


def test_render_graphviz_svg_returns_svg_string_when_graphviz_available():
    regex = RegexBuilder().digit().to_regex()
    output = render_graphviz_svg(regex.elements)
    assert output.startswith("<?xml") or output.startswith("<svg")
    assert "</svg>" in output


def test_module_level_import_falls_back_to_none_when_graphviz_missing(monkeypatch):
    saved_module = sys.modules.pop("graphviz", None)
    real_import = builtins.__import__

    def blocking_import(name, *args, **kwargs):
        if name == "graphviz":
            raise ImportError("graphviz missing")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", blocking_import)
    monkeypatch.setitem(sys.modules, "graphviz", None)
    reloaded = importlib.reload(graphviz_module)
    try:
        regex = RegexBuilder().digit().to_regex()
        with pytest.raises(MissingGraphvizDependencyError):
            reloaded.render_graphviz_svg(regex.elements)
    finally:
        monkeypatch.undo()
        if saved_module is not None:
            sys.modules["graphviz"] = saved_module
        importlib.reload(graphviz_module)


def test_nested_capture_inside_alternation_renders_cluster_inside_fork_merge():
    outer = AnyOfElement(
        children=(
            NamedCaptureElement(name="left", children=(DigitElement(),)),
            NamedCaptureElement(name="right", children=(WordElement(),)),
        )
    )
    output = _dot(outer)
    assert output.count("subgraph cluster_") == 2
    assert '"saved as \\"left\\""' in output
    assert '"saved as \\"right\\""' in output


def test_lookaround_inside_capture_renders_nested_clusters():
    inner = AssertAheadElement(children=(DigitElement(),))
    output = _dot(CaptureElement(children=(inner,)))
    assert '"captured"' in output
    assert '"must be followed by"' in output


def test_visualize_svg_end_to_end_delegates_to_renderer():
    regex = RegexBuilder().digit().to_regex()
    svg = regex.visualize(format="svg", engine="graphviz")
    assert "</svg>" in svg
