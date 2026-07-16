"""Django integration — validate model / form fields against an edify :class:`Pattern`.

Requires the ``django`` extra: ``pip install edify[django]``. Django ships no type
information, so the module is loaded through :func:`importlib.import_module` and its
one used entry point is described by a local :class:`Protocol`.
"""

from __future__ import annotations

import re
from importlib import import_module
from typing import Protocol, cast

from edify.pattern.composition import Pattern


class _RegexValidator(Protocol):
    regex: re.Pattern[str]
    message: str
    code: str

    def __call__(self, value: object) -> None: ...


class _RegexValidatorFactory(Protocol):
    def __call__(self, *, regex: str, message: str, code: str) -> _RegexValidator: ...


def pattern_validator(
    pattern: Pattern,
    message: str | None = None,
    code: str = "invalid",
) -> _RegexValidator:
    """Return a :class:`django.core.validators.RegexValidator` pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a field must match anywhere in.
        message: The error message the validator raises on rejection. Defaults to a
            message that reproduces the pattern's regex string.
        code: The Django validation-error code the validator raises on rejection.
    """
    validators_module = import_module("django.core.validators")
    regex_validator_factory = cast(_RegexValidatorFactory, validators_module.RegexValidator)
    resolved_message = (
        message if message is not None else f"value does not match {pattern.to_regex_string()}"
    )
    return regex_validator_factory(
        regex=pattern.to_regex_string(),
        message=resolved_message,
        code=code,
    )
