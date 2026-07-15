"""FastAPI integration — validate request paths and queries against an edify :class:`Pattern`.

FastAPI is imported lazily inside every public helper so ``import edify.integrations.fastapi``
succeeds even when the framework is not installed. Calls raise
:class:`edify.errors.integration.MissingIntegrationDependencyError` with an actionable
message when the framework is missing.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

from edify.errors.integration import MissingIntegrationDependencyError
from edify.pattern.composition import Pattern


def pattern_query(pattern: Pattern, **query_kwargs: Any) -> Any:
    """Return a :class:`fastapi.Query` value pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a query parameter must match anywhere in.
        query_kwargs: Extra keyword arguments forwarded to :func:`fastapi.Query`.

    Raises:
        MissingIntegrationDependencyError: when the ``fastapi`` package is not installed.
    """
    fastapi_module = _load_fastapi_module()
    default_value = query_kwargs.pop("default", ...)
    return fastapi_module.Query(default_value, pattern=pattern.to_regex_string(), **query_kwargs)


def pattern_path(pattern: Pattern, **path_kwargs: Any) -> Any:
    """Return a :class:`fastapi.Path` value pinned to ``pattern``.

    Args:
        pattern: The :class:`edify.Pattern` a path parameter must match anywhere in.
        path_kwargs: Extra keyword arguments forwarded to :func:`fastapi.Path`.

    Raises:
        MissingIntegrationDependencyError: when the ``fastapi`` package is not installed.
    """
    fastapi_module = _load_fastapi_module()
    default_value = path_kwargs.pop("default", ...)
    return fastapi_module.Path(default_value, pattern=pattern.to_regex_string(), **path_kwargs)


def _load_fastapi_module() -> Any:
    try:
        return import_module("fastapi")
    except ImportError as reason:
        raise MissingIntegrationDependencyError("fastapi") from reason
