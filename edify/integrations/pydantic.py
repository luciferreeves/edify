"""Pydantic integration — validate string fields against an edify :class:`Pattern`.

Pydantic is imported lazily inside every public helper so ``import edify.integrations.pydantic``
succeeds even when the framework is not installed. Calls raise
:class:`edify.errors.integration.MissingIntegrationDependencyError` with an actionable
message when the framework is missing.
"""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import Any

from edify.errors.integration import MissingIntegrationDependencyError
from edify.pattern.composition import Pattern


def pattern_validator(pattern: Pattern) -> Callable[[str], str]:
    """Return a Pydantic-compatible validator callable for ``pattern``.

    The returned callable accepts a string and returns it unchanged when the
    pattern matches; otherwise raises :class:`ValueError` with a message
    Pydantic embeds in its :class:`ValidationError`.

    Args:
        pattern: The :class:`edify.Pattern` the field must match anywhere in.

    Raises:
        MissingIntegrationDependencyError: when the ``pydantic`` package is not installed.
    """
    _ensure_pydantic_is_installed()

    def validate(value: str) -> str:
        if pattern(value):
            return value
        raise ValueError(f"value does not match {pattern.to_regex_string()}")

    return validate


def pattern_field(pattern: Pattern) -> Any:
    """Return an ``Annotated[str, AfterValidator(...)]`` type for use in Pydantic models.

    Args:
        pattern: The :class:`edify.Pattern` the field must match anywhere in.

    Raises:
        MissingIntegrationDependencyError: when the ``pydantic`` package is not installed.
    """
    pydantic_module = _load_pydantic_module()
    validator_callable = pattern_validator(pattern)
    after_validator = pydantic_module.AfterValidator(validator_callable)
    from typing import Annotated

    return Annotated[str, after_validator]


def _load_pydantic_module() -> Any:
    try:
        return import_module("pydantic")
    except ImportError as reason:
        raise MissingIntegrationDependencyError("pydantic") from reason


def _ensure_pydantic_is_installed() -> None:
    _load_pydantic_module()
