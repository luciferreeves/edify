"""The :class:`AnchorsMixin` — chain methods for the ``^`` and ``$`` anchors.

Each anchor may appear at most once per pattern; ``start_of_input`` may
not be added after ``end_of_input``. Violations raise the corresponding
:mod:`edify.errors.anchors` exception.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.leaves import EndOfInputElement, StartOfInputElement
from edify.errors.anchors import (
    CannotDefineStartAfterEndError,
    EndInputAlreadyDefinedError,
    StartInputAlreadyDefinedError,
)


class AnchorsMixin(BuilderProtocol):
    """Provides the ``start_of_input`` and ``end_of_input`` chain methods."""

    def start_of_input(self) -> Self:
        """Return a new builder with a leading ``^`` anchor appended."""
        if self.state.has_defined_start:
            raise StartInputAlreadyDefinedError()
        if self.state.has_defined_end:
            raise CannotDefineStartAfterEndError()
        state_with_flag = self.state.with_start_defined()
        new_state = state_with_flag.with_element_added_to_top(StartOfInputElement())
        return self.with_state(new_state)

    def end_of_input(self) -> Self:
        """Return a new builder with a trailing ``$`` anchor appended."""
        if self.state.has_defined_end:
            raise EndInputAlreadyDefinedError()
        state_with_flag = self.state.with_end_defined()
        new_state = state_with_flag.with_element_added_to_top(EndOfInputElement())
        return self.with_state(new_state)
