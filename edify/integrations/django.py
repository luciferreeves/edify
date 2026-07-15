"""Django integration — validate model / form fields against an edify :class:`Pattern`.

Django is imported lazily inside every public helper so ``import edify.integrations.django``
succeeds even when the framework is not installed. Calls raise
:class:`edify.errors.integration.MissingIntegrationDependencyError` with an actionable
message when the framework is missing.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

from edify.errors.integration import MissingIntegrationDependencyError
from edify.pattern.composition import Pattern


def pattern_validator(pattern: Pattern, message: str | None = None, code: str = "invalid") -> Any:
    """Return a :class:`django.core.validators.RegexValidator` pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a field must match anywhere in.
        message: The error message the validator raises on rejection. Defaults to a
            message that reproduces the pattern's regex string.
        code: The Django validation-error code the validator raises on rejection.

    Raises:
        MissingIntegrationDependencyError: when the ``django`` package is not installed.
    """
    validators_module = _load_django_validators_module()
    resolved_message = (
        message if message is not None else f"value does not match {pattern.to_regex_string()}"
    )
    return validators_module.RegexValidator(
        regex=pattern.to_regex_string(),
        message=resolved_message,
        code=code,
    )


def _load_django_validators_module() -> Any:
    try:
        return import_module("django.core.validators")
    except ImportError as reason:
        raise MissingIntegrationDependencyError("django") from reason
