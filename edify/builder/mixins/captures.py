"""The :class:`CapturesMixin` — chain methods for capture groups and back-references.

``capture`` and ``named_capture`` push a new frame onto the builder's stack;
the frame closes when the user calls ``.end()`` later. Back-reference
methods validate against the names / indices declared so far and append
their element to the top frame.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import StackFrame
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.errors.captures import InvalidTotalCaptureGroupsIndexError
from edify.errors.input import MustBeOneCharacterError
from edify.errors.naming import (
    CannotCreateDuplicateNamedGroupError,
    NamedGroupDoesNotExistError,
    NameNotValidError,
)
from edify.validate.names import is_valid_group_name


class CapturesMixin(BuilderProtocol):
    """Provides capture/named-capture/back-reference chain methods."""

    def capture(self) -> Self:
        """Return a new builder with a numbered-capture frame opened."""
        new_frame = StackFrame(type_node=CaptureElement())
        state_with_frame = self.state.with_frame_pushed(new_frame)
        state_with_count = state_with_frame.with_capture_group_count_incremented()
        return self.with_state(state_with_count)

    def named_capture(self, name: str) -> Self:
        """Return a new builder with a named-capture frame opened under ``name``."""
        _validate_new_named_group(name, self.state.named_groups)
        new_frame = StackFrame(type_node=NamedCaptureElement(name=name))
        state_with_frame = self.state.with_frame_pushed(new_frame)
        state_with_count = state_with_frame.with_capture_group_count_incremented()
        state_with_name = state_with_count.with_named_group_added(name)
        return self.with_state(state_with_name)

    def back_reference(self, index: int) -> Self:
        """Return a new builder with a numbered back-reference to capture ``index`` appended."""
        _ensure_capture_index_in_range(index, self.state.total_capture_groups)
        element = BackReferenceElement(index=index)
        new_state = self.state.with_element_added_to_top(element)
        return self.with_state(new_state)

    def named_back_reference(self, name: str) -> Self:
        """Return a new builder with a named back-reference to ``name`` appended."""
        _ensure_named_group_exists(name, self.state.named_groups)
        element = NamedBackReferenceElement(name=name)
        new_state = self.state.with_element_added_to_top(element)
        return self.with_state(new_state)


def _validate_new_named_group(name: str, existing_names: tuple[str, ...]) -> None:
    """Raise the appropriate naming error if ``name`` cannot be declared as a new named group."""
    if len(name) == 0:
        raise MustBeOneCharacterError("Name")
    if name in existing_names:
        raise CannotCreateDuplicateNamedGroupError(name)
    if not is_valid_group_name(name):
        raise NameNotValidError(name)


def _ensure_capture_index_in_range(index: int, total_capture_groups: int) -> None:
    """Raise :class:`InvalidTotalCaptureGroupsIndexError` if ``index`` is out of declared range."""
    if 1 <= index <= total_capture_groups:
        return
    raise InvalidTotalCaptureGroupsIndexError(index, total_capture_groups)


def _ensure_named_group_exists(name: str, declared_names: tuple[str, ...]) -> None:
    """Raise :class:`NamedGroupDoesNotExistError` when ``name`` was never declared."""
    if name in declared_names:
        return
    raise NamedGroupDoesNotExistError(name)
