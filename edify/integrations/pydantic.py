"""Pydantic integration — validate string fields against an edify :class:`Pattern`.

Requires the ``pydantic`` extra: ``pip install edify[pydantic]``. Importing this module
without the framework installed raises :class:`ImportError` at import time.

Typical usage:

.. code-block:: python

    from typing import Annotated
    from pydantic import AfterValidator, BaseModel
    from edify.integrations.pydantic import pattern_validator
    from edify.library import email

    class Contact(BaseModel):
        address: Annotated[str, AfterValidator(pattern_validator(email))]
"""

from __future__ import annotations

from collections.abc import Callable

from edify.errors.integration import PatternDidNotMatchError
from edify.pattern.composition import Pattern


def pattern_validator(pattern: Pattern) -> Callable[[str], str]:
    """Return a Pydantic-compatible validator callable for ``pattern``.

    The returned callable accepts a string and returns it unchanged when the
    pattern matches; otherwise raises :class:`edify.errors.integration.PatternDidNotMatchError`
    (a :class:`ValueError` subclass) that Pydantic embeds in its :class:`ValidationError`.

    Args:
        pattern: The :class:`edify.Pattern` the field must match anywhere in.
    """
    pattern_source = pattern.to_regex_string()

    def validate(value: str) -> str:
        if pattern(value):
            return value
        raise PatternDidNotMatchError(pattern_source, value)

    return validate
