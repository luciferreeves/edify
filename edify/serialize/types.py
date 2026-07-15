"""JSON-value type used by every canonical (de)serialization function."""

from __future__ import annotations

JSONPrimitive = str | int | float | bool | None
"""One of the primitive scalar values a JSON payload may carry."""

JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
"""Any value that appears anywhere in a canonical Pattern serialization payload."""
