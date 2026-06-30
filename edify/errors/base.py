"""Base exception class for every error edify raises.

Subclassing :class:`Exception` keeps any existing ``except Exception`` blocks
working — the typed hierarchy is additive. Catch :class:`EdifyError` to react
to any error the library produces without binding to the narrower subclasses.
"""

from __future__ import annotations


class EdifyError(Exception):
    """Base class for every exception edify raises."""
