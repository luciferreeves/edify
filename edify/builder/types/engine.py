"""Type alias for the ``engine`` kwarg accepted by every builder terminal."""

from __future__ import annotations

from typing import Literal

Engine = Literal["re", "regex"]
"""The compilation-backend identifier accepted by :meth:`edify.RegexBuilder.to_regex`."""
