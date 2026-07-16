"""FastAPI integration — validate request paths and queries against an edify :class:`Pattern`.

Requires the ``fastapi`` extra: ``pip install edify[fastapi]``. Importing this module
without the framework installed raises :class:`ImportError` at import time.
"""

from __future__ import annotations

from typing import cast

import fastapi
import fastapi.params

from edify.pattern.composition import Pattern


def pattern_query(
    pattern: Pattern,
    default: str | None = None,
    description: str | None = None,
) -> fastapi.params.Query:
    """Return a :class:`fastapi.Query` value pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a query parameter must match anywhere in.
        default: Optional default value; when None the parameter is required.
        description: Optional OpenAPI description forwarded to :func:`fastapi.Query`.
    """
    pattern_source = pattern.to_regex_string()
    default_value = default if default is not None else ...
    query = fastapi.Query(default_value, pattern=pattern_source, description=description)
    return cast(fastapi.params.Query, query)


def pattern_path(pattern: Pattern, description: str | None = None) -> fastapi.params.Path:
    """Return a :class:`fastapi.Path` value pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a path parameter must match anywhere in.
        description: Optional OpenAPI description forwarded to :func:`fastapi.Path`.
    """
    pattern_source = pattern.to_regex_string()
    path = fastapi.Path(..., pattern=pattern_source, description=description)
    return cast(fastapi.params.Path, path)
