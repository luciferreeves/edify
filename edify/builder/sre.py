"""Typed access to the stdlib private ``re`` parser and its opcode constants.

The stdlib exposes its regex parser under ``re._parser`` and the opcode
constants under ``re._constants``; neither carries type information. This module
loads both through :func:`importlib.import_module` (typed :class:`~types.ModuleType`)
and re-exports exactly the surface the reverse parser needs, with every value
pinned to a concrete type. It is the single place in the package that touches the
private ``re`` internals.
"""

from __future__ import annotations

from importlib import import_module
from typing import TypeAlias, cast

_constants = import_module("re._constants")
_parser = import_module("re._parser")

SreArgument: TypeAlias = (
    int
    | tuple[int, int]
    | tuple[int, int, "SrePattern"]
    | tuple[int | None, int, int, "SrePattern"]
    | tuple[None, list["SrePattern"]]
    | tuple[int, "SrePattern"]
    | list["SreNode"]
    | None
)
"""Union of every argument shape the parser emits on the second slot of a node."""

SreNode: TypeAlias = tuple[int, SreArgument]
"""One ``(opcode, argument)`` node produced by :func:`parse`."""

SrePattern: TypeAlias = list[SreNode]
"""Sequence of :data:`SreNode` items."""


def _const(name: str) -> int:
    return int(getattr(_constants, name))


MAXREPEAT = _const("MAXREPEAT")

LITERAL = _const("LITERAL")
ANY = _const("ANY")
AT = _const("AT")
IN = _const("IN")
MAX_REPEAT = _const("MAX_REPEAT")
MIN_REPEAT = _const("MIN_REPEAT")
SUBPATTERN = _const("SUBPATTERN")
BRANCH = _const("BRANCH")
ASSERT = _const("ASSERT")
ASSERT_NOT = _const("ASSERT_NOT")
RANGE = _const("RANGE")
CATEGORY = _const("CATEGORY")

AT_BEGINNING = _const("AT_BEGINNING")
AT_BEGINNING_STRING = _const("AT_BEGINNING_STRING")
AT_END = _const("AT_END")
AT_END_STRING = _const("AT_END_STRING")
AT_BOUNDARY = _const("AT_BOUNDARY")
AT_NON_BOUNDARY = _const("AT_NON_BOUNDARY")

CATEGORY_DIGIT = _const("CATEGORY_DIGIT")
CATEGORY_NOT_DIGIT = _const("CATEGORY_NOT_DIGIT")
CATEGORY_WORD = _const("CATEGORY_WORD")
CATEGORY_NOT_WORD = _const("CATEGORY_NOT_WORD")
CATEGORY_SPACE = _const("CATEGORY_SPACE")
CATEGORY_NOT_SPACE = _const("CATEGORY_NOT_SPACE")


def parse(pattern_text: str) -> SrePattern:
    """Return ``pattern_text`` parsed into a list of ``(opcode, argument)`` nodes."""
    raw_result = _parser.parse(pattern_text)
    return cast(SrePattern, list(raw_result))
