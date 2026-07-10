"""Shared dataclasses used by the introspection renderers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Diagram:
    """Rectangular block of ASCII rows with a designated horizontal entry row.

    Attributes:
        rows: Uniform-width lines that make up the diagram.
        entry_row: 0-indexed row where left/right connectors attach.
        width: Character width shared by every row.
    """

    rows: tuple[str, ...]
    entry_row: int
    width: int


@dataclass(frozen=True)
class Emission:
    """DOT lines for one element plus the node ids where the horizontal flow enters and exits.

    Attributes:
        entry_id: DOT node id that upstream edges attach to.
        exit_id: DOT node id that downstream edges leave from.
        lines: Indented DOT source lines describing the subgraph.
    """

    entry_id: str
    exit_id: str
    lines: tuple[str, ...]
