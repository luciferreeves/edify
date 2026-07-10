"""Exceptions raised by the :class:`edify.result.regex.Regex` introspection API."""

from __future__ import annotations

from edify.errors.context import capture_caller_context
from edify.errors.formatting import format_error, format_note_line, format_pointer_block
from edify.errors.syntax import EdifySyntaxError

_SUPPORTED_FORMATS = ("ascii", "svg")
_SUPPORTED_ENGINES_BY_FORMAT: dict[str, tuple[str, ...]] = {
    "ascii": ("ascii",),
    "svg": ("graphviz",),
}


class UnsupportedVisualizationFormatError(EdifySyntaxError):
    """Raised when ``Regex.visualize(format=...)`` receives an unknown format.

    Args:
        received_format: The format string the caller passed.
    """

    def __init__(self, received_format: str) -> None:
        caller_context = capture_caller_context()
        trigger_block = ""
        if caller_context is not None:
            trigger_block = format_pointer_block(caller_context, "unknown format here")
        supported = ", ".join(f"'{fmt}'" for fmt in _SUPPORTED_FORMATS)
        note_line = format_note_line(
            f"Regex.visualize accepts one of {supported}; received {received_format!r}."
        )
        message = format_error(
            f"unsupported visualization format {received_format!r}",
            trigger_block + "\n" + note_line if trigger_block else note_line,
            "help: pass format='ascii' for a text railroad diagram, "
            "or format='svg' for a Graphviz-rendered SVG.",
        )
        super().__init__(message)


class UnsupportedVisualizationEngineError(EdifySyntaxError):
    """Raised when ``Regex.visualize(engine=...)`` does not pair with the chosen format.

    Args:
        received_format: The format string the caller passed.
        received_engine: The engine string the caller passed.
    """

    def __init__(self, received_format: str, received_engine: str) -> None:
        caller_context = capture_caller_context()
        trigger_block = ""
        if caller_context is not None:
            trigger_block = format_pointer_block(caller_context, "engine does not match format")
        supported = _SUPPORTED_ENGINES_BY_FORMAT.get(received_format, ())
        supported_list = ", ".join(f"'{engine}'" for engine in supported) or "(none)"
        note_line = format_note_line(
            f"format={received_format!r} pairs with engine in {supported_list}; "
            f"received engine={received_engine!r}."
        )
        preferred_engine = supported_list.split(",")[0].strip() if supported else "ascii"
        message = format_error(
            f"engine {received_engine!r} does not pair with format {received_format!r}",
            trigger_block + "\n" + note_line if trigger_block else note_line,
            f"help: pass engine={preferred_engine!r}.",
        )
        super().__init__(message)


class MissingGraphvizDependencyError(EdifySyntaxError):
    """Raised when ``Regex.visualize(format='svg')`` is called without graphviz installed."""

    def __init__(self) -> None:
        caller_context = capture_caller_context()
        trigger_block = ""
        if caller_context is not None:
            trigger_block = format_pointer_block(
                caller_context, "graphviz dependency required here"
            )
        note_line = format_note_line(
            "the graphviz Python package is required to render SVG diagrams; "
            "it is not installed in this environment."
        )
        message = format_error(
            "graphviz optional dependency is not installed",
            trigger_block + "\n" + note_line if trigger_block else note_line,
            "help: install with `pip install 'edify[graphviz]'` "
            "or `uv add edify --extra graphviz`.",
        )
        super().__init__(message)
