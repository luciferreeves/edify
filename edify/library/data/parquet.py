"""``parquet`` — Apache Parquet file signature shape."""

from __future__ import annotations

from edify import Pattern

parquet = Pattern().start_of_input().string("PAR1").zero_or_more().any_char().end_of_input()
"""Callable :class:`Pattern` for an Apache Parquet file (``PAR1`` magic prefix)."""
