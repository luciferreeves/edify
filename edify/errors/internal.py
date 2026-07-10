"""Exception classes for internal-consistency violations inside edify."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class UnknownElementTypeError(EdifySyntaxError):
    """Raised when the compile dispatcher receives an element class it does not recognise.

    Args:
        element_type_name: The class name that was not registered on the dispatch table.
    """

    def __init__(self, element_type_name: str) -> None:
        message = compose_annotated_message(
            summary=f"unknown element type {element_type_name!r} reached the compiler",
            trigger_hint="pattern compiled here",
            note=(
                f"the compile dispatcher has no rule for {element_type_name}; either the "
                "element is misconstructed or a compile handler is missing for this class."
            ),
            help_line=(
                "help: this is an internal edify bug; please file it at "
                "https://github.com/luciferreeves/edify/issues with the pattern that "
                "triggered the error."
            ),
        )
        super().__init__(message)


class NonFusableElementError(EdifySyntaxError):
    """Raised when the char-class fuser is handed an element it cannot fuse.

    Args:
        element_type_name: The class name that the fuser refused.
    """

    def __init__(self, element_type_name: str) -> None:
        message = compose_annotated_message(
            summary=f"cannot fuse element {element_type_name!r} into a character class",
            trigger_hint="pattern compiled here",
            note=(
                "the character-class fuser accepts only character-shaped elements "
                f"(CharElement, RangeElement, AnyOfCharsElement); {element_type_name} is not one of them."
            ),
            help_line=(
                "help: this is an internal edify bug; please file it at "
                "https://github.com/luciferreeves/edify/issues with the pattern that "
                "triggered the error."
            ),
        )
        super().__init__(message)


class UnexpectedFrameTypeError(EdifySyntaxError):
    """Raised when a stack frame's anchor element is not a recognised container kind.

    Args:
        element_type_name: The class name held by the offending stack frame.
    """

    def __init__(self, element_type_name: str) -> None:
        message = compose_annotated_message(
            summary=f"stack frame anchored at unexpected element {element_type_name!r}",
            trigger_hint="pattern touched here",
            note=(
                "builder frames must anchor at a container element such as CaptureElement, "
                f"NamedCaptureElement, GroupElement, AnyOfElement, or a lookaround; "
                f"{element_type_name} is not one of the accepted container kinds."
            ),
            help_line=(
                "help: this is an internal edify bug; please file it at "
                "https://github.com/luciferreeves/edify/issues with the pattern that "
                "triggered the error."
            ),
        )
        super().__init__(message)


class FailedToCompileRegexError(EdifySyntaxError):
    """Raised when the underlying ``re`` engine rejects the emitted pattern.

    Args:
        underlying_error_message: The message string reported by ``re.compile``.
    """

    def __init__(self, underlying_error_message: str) -> None:
        message = compose_annotated_message(
            summary="the emitted regex was rejected by the re engine",
            trigger_hint=".to_regex() / .to_regex_string() called here",
            note=(
                f"re.compile refused the pattern: {underlying_error_message}"
            ),
            help_line=(
                "help: inspect the raw pattern with .to_regex_string() and cross-check "
                "quantifier / group placement; if the pattern looks correct, please file "
                "the issue at https://github.com/luciferreeves/edify/issues."
            ),
        )
        super().__init__(message)
