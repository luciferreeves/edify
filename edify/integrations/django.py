"""Django integration — validate model / form fields against an edify :class:`Pattern`.

Requires the ``django`` extra: ``pip install edify[django]``. Importing this module
without the framework installed raises :class:`ImportError` at import time.
"""

from __future__ import annotations

import django.core.validators

from edify.pattern.composition import Pattern


def pattern_validator(
    pattern: Pattern,
    message: str | None = None,
    code: str = "invalid",
) -> django.core.validators.RegexValidator:
    """Return a :class:`django.core.validators.RegexValidator` pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a field must match anywhere in.
        message: The error message the validator raises on rejection. Defaults to a
            message that reproduces the pattern's regex string.
        code: The Django validation-error code the validator raises on rejection.
    """
    resolved_message = (
        message if message is not None else f"value does not match {pattern.to_regex_string()}"
    )
    return django.core.validators.RegexValidator(
        regex=pattern.to_regex_string(),
        message=resolved_message,
        code=code,
    )
