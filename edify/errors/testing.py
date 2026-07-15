"""Exceptions raised by the pattern-testing helpers on the builder surface."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message


class PatternDidNotMatchInputsError(AssertionError):
    """Raised by :meth:`assert_matches` when one or more expected inputs did not match."""

    def __init__(self, pattern_source: str, missing_matches: tuple[str, ...]) -> None:
        listed = ", ".join(repr(item) for item in missing_matches)
        summary = (
            f"pattern {pattern_source!r} did not match {len(missing_matches)} expected "
            f"input(s): {listed}"
        )
        message = compose_annotated_message(
            summary=summary,
            trigger_hint=".assert_matches([...]) called here",
            note=(
                "every string in the argument list must match the pattern to satisfy the "
                "assertion; the listed inputs were rejected."
            ),
            help_line=(
                "help: adjust the pattern to accept these inputs, or drop them from the "
                "assertion list."
            ),
        )
        super().__init__(message)
        self.missing_matches = missing_matches


class PatternMatchedRejectedInputsError(AssertionError):
    """Raised by :meth:`assert_rejects` when one or more inputs matched unexpectedly."""

    def __init__(self, pattern_source: str, unexpected_matches: tuple[str, ...]) -> None:
        listed = ", ".join(repr(item) for item in unexpected_matches)
        summary = (
            f"pattern {pattern_source!r} matched {len(unexpected_matches)} input(s) that "
            f"were expected to be rejected: {listed}"
        )
        message = compose_annotated_message(
            summary=summary,
            trigger_hint=".assert_rejects([...]) called here",
            note=(
                "every string in the argument list must be rejected by the pattern to satisfy "
                "the assertion; the listed inputs matched instead."
            ),
            help_line=(
                "help: tighten the pattern so these inputs no longer match, or drop them from "
                "the assertion list."
            ),
        )
        super().__init__(message)
        self.unexpected_matches = unexpected_matches
