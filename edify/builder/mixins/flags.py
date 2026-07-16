"""The :class:`FlagsMixin` — chain methods that toggle pattern-global regex flags.

Each method returns a new builder whose flags snapshot has the corresponding
field enabled. Flags are pattern-global — position in the chain does not
matter.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.protocol import BuilderProtocol


class FlagsMixin(BuilderProtocol):
    """Provides the six flag-toggle chain methods on the builder."""

    def ascii_only(self) -> Self:
        """Return a new builder with the ``re.A`` flag enabled."""
        new_flags = self.state.flags.with_ascii_only()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)

    def debug(self) -> Self:
        """Return a new builder with the ``re.DEBUG`` flag enabled."""
        new_flags = self.state.flags.with_debug()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)

    def ignore_case(self) -> Self:
        """Return a new builder with the ``re.I`` flag enabled."""
        new_flags = self.state.flags.with_ignore_case()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)

    def multi_line(self) -> Self:
        """Return a new builder with the ``re.M`` flag enabled."""
        new_flags = self.state.flags.with_multiline()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)

    def dot_all(self) -> Self:
        """Return a new builder with the ``re.S`` flag enabled."""
        new_flags = self.state.flags.with_dotall()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)

    def verbose(self) -> Self:
        """Return a new builder with the ``re.X`` flag enabled."""
        new_flags = self.state.flags.with_verbose()
        new_state = self.state.with_flags(new_flags)
        return self.with_state(new_state)
