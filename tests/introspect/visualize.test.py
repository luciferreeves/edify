"""Tests for the visualize dispatcher in :mod:`edify.introspect.visualize`."""

import pytest

from edify import RegexBuilder
from edify.elements.types.leaves import DigitElement
from edify.errors.introspect import (
    UnsupportedVisualizationEngineError,
    UnsupportedVisualizationFormatError,
)
from edify.introspect.visualize import visualize_elements


def _digit_regex():
    return RegexBuilder().digit().to_regex()


def test_default_format_and_engine_produce_ascii_railroad_output():
    output = visualize_elements((DigitElement(),))
    assert "| START |" in output
    assert "| digit |" in output
    assert "| END |" in output


def test_explicit_ascii_format_and_engine_produce_ascii_railroad_output():
    output = visualize_elements((DigitElement(),), format="ascii", engine="ascii")
    assert "| digit |" in output


def test_ascii_format_with_wrong_engine_raises_engine_error():
    with pytest.raises(UnsupportedVisualizationEngineError):
        visualize_elements((DigitElement(),), format="ascii", engine="graphviz")


def test_svg_format_with_graphviz_engine_produces_svg_output():
    regex = _digit_regex()
    output = visualize_elements(regex.elements, format="svg", engine="graphviz")
    assert "</svg>" in output


def test_svg_format_with_wrong_engine_raises_engine_error():
    with pytest.raises(UnsupportedVisualizationEngineError):
        visualize_elements((DigitElement(),), format="svg", engine="ascii")


def test_unknown_format_raises_format_error():
    with pytest.raises(UnsupportedVisualizationFormatError):
        visualize_elements((DigitElement(),), format="pdf")


def test_unknown_format_error_names_the_received_format_in_message():
    with pytest.raises(UnsupportedVisualizationFormatError) as excinfo:
        visualize_elements((DigitElement(),), format="mermaid")
    assert "'mermaid'" in str(excinfo.value)


def test_engine_error_names_both_format_and_engine_in_message():
    with pytest.raises(UnsupportedVisualizationEngineError) as excinfo:
        visualize_elements((DigitElement(),), format="ascii", engine="mermaid")
    message = str(excinfo.value)
    assert "'ascii'" in message
    assert "'mermaid'" in message


def test_regex_visualize_end_to_end_defaults_to_ascii():
    regex = _digit_regex()
    output = regex.visualize()
    assert "| digit |" in output


def test_regex_visualize_svg_end_to_end():
    regex = _digit_regex()
    output = regex.visualize(format="svg", engine="graphviz")
    assert "</svg>" in output


def test_regex_visualize_rejects_unknown_format_end_to_end():
    regex = _digit_regex()
    with pytest.raises(UnsupportedVisualizationFormatError):
        regex.visualize(format="dot")


def test_regex_visualize_rejects_engine_mismatch_end_to_end():
    regex = _digit_regex()
    with pytest.raises(UnsupportedVisualizationEngineError):
        regex.visualize(format="svg", engine="ascii")


def test_empty_elements_still_render_start_and_end():
    output = visualize_elements(())
    assert "START" in output
    assert "END" in output
