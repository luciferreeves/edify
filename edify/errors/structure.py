"""Exception classes raised for builder-frame structural errors."""

from __future__ import annotations

from dataclasses import dataclass

from edify.errors.context import CallerContext
from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


@dataclass(frozen=True)
class OpenFrameInfo:
    """One frame in the open-frame stack, named for error rendering.

    Attributes:
        kind: Human-readable frame type (``"capture"``, ``"assert_ahead"``, ...).
        opened_at: Caller context for the chain call that opened the frame;
            ``None`` when the location could not be captured.
    """

    kind: str
    opened_at: CallerContext | None


class CannotEndWhileBuildingRootExpressionError(EdifySyntaxError):
    """Raised when ``.end()`` is called on a builder whose only open frame is the root."""

    def __init__(self) -> None:
        message = compose_annotated_message(
            summary="cannot .end() while building the root expression",
            trigger_hint=".end() called here",
            note=(
                ".end() closes the innermost open frame, but the root expression has no "
                "matching opener; there is no frame to close."
            ),
            help_line=(
                "help: remove this .end() call, or open a frame first with "
                ".capture(), .named_capture(name), .group(), .any_of(), or a lookaround."
            ),
        )
        super().__init__(message)


class CannotCallSubexpressionError(EdifySyntaxError):
    """Raised when ``.subexpression(expression)`` is given an expression with open frames.

    Args:
        open_frames: The stack of frames that remain open on the subexpression, in
            innermost-first order.
    """

    def __init__(self, open_frames: tuple[OpenFrameInfo, ...]) -> None:
        rendered_stack = _format_open_frame_stack(open_frames)
        innermost_kind = open_frames[0].kind
        message = compose_annotated_message(
            summary="cannot merge a subexpression that has an unclosed frame",
            trigger_hint="subexpression merged here",
            note=(
                f"the subexpression still has {len(open_frames)} open frame(s); "
                "only fully-closed expressions can be merged into another builder.\n"
                f"open frames (innermost first):\n{rendered_stack}"
            ),
            help_line=(
                f"help: add a matching .end() call for each open frame — start by closing "
                f"the innermost .{innermost_kind}() frame — before passing the subexpression "
                "to .subexpression(...)."
            ),
        )
        super().__init__(message)
        self.open_frames = open_frames


def _format_open_frame_stack(open_frames: tuple[OpenFrameInfo, ...]) -> str:
    rendered_lines: list[str] = []
    for depth, frame_info in enumerate(open_frames, start=1):
        rendered_lines.append(_format_open_frame_line(depth, frame_info))
    return "\n".join(rendered_lines)


def _format_open_frame_line(depth: int, frame_info: OpenFrameInfo) -> str:
    prefix = f"   {depth}. .{frame_info.kind}()"
    if frame_info.opened_at is None:
        return f"{prefix} — opened at <unknown>"
    context = frame_info.opened_at
    return f"{prefix} — opened at {context.filename}:{context.lineno}:{context.colno}"
