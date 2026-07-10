"""Exception classes raised when a builder method receives invalid input."""

from __future__ import annotations

from edify.errors.formatting import compose_annotated_message
from edify.errors.syntax import EdifySyntaxError


class MustBeAStringError(EdifySyntaxError):
    """Raised when a builder argument is required to be a string but is not.

    Args:
        label: What the argument is called in the API (e.g. ``"Name"``).
        actual_type_name: The class name of the value the caller passed.
    """

    def __init__(self, label: str, actual_type_name: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=f"{label} must be a string (got {actual_type_name})",
            trigger_hint=f"{lowered} passed here",
            note=(
                f"this builder method expects {lowered} to be a str, but the caller "
                f"passed a value of type {actual_type_name}."
            ),
            help_line=(
                f"help: convert the value with str(...) or pass a string literal for {lowered}."
            ),
        )
        super().__init__(message)


class MustBeOneCharacterError(EdifySyntaxError):
    """Raised when a builder argument must have a length of at least one character.

    Args:
        label: What the argument is called in the API.
    """

    def __init__(self, label: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=f"{label} must be one character long",
            trigger_hint=f"empty {lowered} passed here",
            note=(
                f"this builder method needs {lowered} to be a non-empty string; an "
                "empty string has no character to match."
            ),
            help_line=(
                f"help: pass a single-character string for {lowered} (e.g. \"a\")."
            ),
        )
        super().__init__(message)


class MustBeSingleCharacterError(EdifySyntaxError):
    """Raised when a builder argument must be exactly one character long.

    Args:
        label: What the argument is called in the API.
        actual_type_name: The class name of the value the caller passed.
    """

    def __init__(self, label: str, actual_type_name: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=f"{label} must be a single character (got {actual_type_name})",
            trigger_hint=f"{lowered} passed here",
            note=(
                f"this builder method expects {lowered} to be a one-character string; "
                f"a value of type {actual_type_name} does not qualify."
            ),
            help_line=(
                f"help: pass a single-character string for {lowered} "
                "(e.g. \"a\" — not \"ab\" or a non-string value)."
            ),
        )
        super().__init__(message)


class MustBePositiveIntegerError(EdifySyntaxError):
    """Raised when a builder argument must be a positive integer (``> 0``).

    Args:
        label: What the argument is called in the API.
    """

    def __init__(self, label: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=f"{label} must be a positive integer",
            trigger_hint=f"{lowered} passed here",
            note=(
                f"this quantifier bound needs {lowered} to be an int greater than or "
                "equal to 1; zero and negative counts have no matching semantics."
            ),
            help_line=(
                f"help: pass an int >= 1 for {lowered}; use .optional() if you meant "
                "zero-or-one."
            ),
        )
        super().__init__(message)


class MustBeIntegerGreaterThanZeroError(EdifySyntaxError):
    """Raised when a builder argument must be an integer strictly greater than zero.

    Args:
        label: What the argument is called in the API.
    """

    def __init__(self, label: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=f"{label} must be an integer greater than zero",
            trigger_hint=f"{lowered} passed here",
            note=(
                f"this quantifier bound needs {lowered} to be an int strictly greater "
                "than 0; zero and negative counts have no matching semantics."
            ),
            help_line=(
                f"help: pass an int > 0 for {lowered}; use .optional() if you meant "
                "zero-or-one."
            ),
        )
        super().__init__(message)


class MustBeInstanceError(EdifySyntaxError):
    """Raised when a builder argument must be an instance of a specific class.

    Args:
        label: What the argument is called in the API.
        actual_type_name: The class name of the value the caller passed.
        expected_class_name: The class name the caller was expected to pass.
    """

    def __init__(self, label: str, actual_type_name: str, expected_class_name: str) -> None:
        lowered = label.lower()
        message = compose_annotated_message(
            summary=(
                f"{label} must be an instance of {expected_class_name} "
                f"(got {actual_type_name})"
            ),
            trigger_hint=f"{lowered} passed here",
            note=(
                f"this method requires {lowered} to be an instance of {expected_class_name}; "
                f"a value of type {actual_type_name} cannot participate in the composition."
            ),
            help_line=(
                f"help: construct {lowered} via {expected_class_name}(...) or one of the "
                "top-level factory functions before passing it here."
            ),
        )
        super().__init__(message)


class MustHaveASmallerValueError(EdifySyntaxError):
    """Raised when the first character argument must order before the second.

    Args:
        first: The lower-bound character supplied.
        second: The upper-bound character supplied.
    """

    def __init__(self, first: str, second: str) -> None:
        first_codepoint = ord(first)
        second_codepoint = ord(second)
        message = compose_annotated_message(
            summary=(
                f"range bounds are inverted: {first!r} must come before {second!r} "
                "in codepoint order"
            ),
            trigger_hint="inverted range declared here",
            note=(
                f"a character range needs the first bound to have a strictly smaller "
                f"codepoint than the second; {first!r} = {first_codepoint} and "
                f"{second!r} = {second_codepoint}."
            ),
            help_line=(
                f"help: swap the bounds so the smaller character comes first "
                f"(e.g. range_of({second!r}, {first!r}))."
            ),
        )
        super().__init__(message)


class MustBeLessThanError(EdifySyntaxError):
    """Raised when a numeric argument must order strictly before another.

    Args:
        first_label: What the smaller-bound argument is called in the API.
        second_label: What the larger-bound argument is called in the API.
    """

    def __init__(self, first_label: str, second_label: str) -> None:
        message = compose_annotated_message(
            summary=f"{first_label} must be less than {second_label}",
            trigger_hint="inverted bounds declared here",
            note=(
                f"the pair ({first_label}, {second_label}) forms a range; "
                f"{first_label} must be strictly less than {second_label} for the range "
                "to contain any matches."
            ),
            help_line=(
                f"help: swap the two arguments so {first_label} is the smaller value."
            ),
        )
        super().__init__(message)


class MustBeAtLeastTwoOperandsError(EdifySyntaxError):
    """Raised when a variadic factory needs at least two operands but got fewer.

    Args:
        label: The name of the factory function (e.g. ``"any_of"``).
    """

    def __init__(self, label: str) -> None:
        message = compose_annotated_message(
            summary=f"{label} requires at least two operands",
            trigger_hint=f"{label} called here",
            note=(
                f"{label} builds an alternation between two-or-more branches; passing "
                "fewer than two operands leaves nothing to alternate between."
            ),
            help_line=(
                f"help: pass at least two Pattern operands to {label}(...); "
                "if you have only one alternative, use it directly without an alternation."
            ),
        )
        super().__init__(message)


class MustBeAtLeastOneLiteralError(EdifySyntaxError):
    """Raised when a variadic literal-alternation chain method got zero literals.

    Args:
        label: The name of the chain method (e.g. ``"one_of"``).
    """

    def __init__(self, label: str) -> None:
        message = compose_annotated_message(
            summary=f"{label} requires at least one literal",
            trigger_hint=f"{label} called here",
            note=(
                f"{label} builds a literal alternation; without any string literal, "
                "the chain method has no branch to add."
            ),
            help_line=(
                f"help: pass one or more string literals to {label}(...) "
                "(e.g. .one_of('cat', 'dog'))."
            ),
        )
        super().__init__(message)
