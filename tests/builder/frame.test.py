"""Test for the ``UnexpectedFrameTypeError`` raise when an AST is built incorrectly."""

import pytest

from edify import RegexBuilder
from edify.builder.types.frame import StackFrame
from edify.elements.types.leaves import DigitElement
from edify.errors.internal import UnexpectedFrameTypeError


def test_end_on_unrecognised_frame_type_raises():
    builder = RegexBuilder().capture()
    stray_frame = StackFrame(type_node=DigitElement())
    new_state = builder._state.with_frame_pushed(stray_frame)
    builder_with_stray = builder._with_state(new_state)
    with pytest.raises(UnexpectedFrameTypeError, match="DigitElement"):
        builder_with_stray.end()
