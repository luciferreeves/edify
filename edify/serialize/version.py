"""Schema-version marker for the canonical :class:`Pattern` serialization.

The version is embedded under the ``"edify"`` key in every ``to_dict`` /
``to_json`` output and validated on load. The 1.0 release ships version ``0``
as experimental — the concrete AST shape may change without a deprecation
cycle until it is promoted to ``1`` in a later release.
"""

from __future__ import annotations

SCHEMA_VERSION = 0
"""The canonical-dict schema version emitted and accepted by this build.

Version ``0`` is experimental. Consumers should not rely on the concrete
AST shape across releases until the version is promoted.
"""
