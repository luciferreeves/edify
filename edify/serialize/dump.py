"""Serialize a :class:`Pattern` into the canonical dict form.

The canonical shape is::

    {
        "edify": <schema-version>,
        "pattern": <root-element-dict>,
        "flags": <flag-name-to-True map>,  # only when any flag is set
    }

Every element dict carries a ``"kind"`` string (see :mod:`edify.serialize.kinds`)
and the fields that element declares — ``value`` for character literals,
``child`` for quantifiers, ``children`` for containers, ``times``/``lower``/
``upper`` for numeric quantifiers, ``name``/``index`` for captures.
"""

from __future__ import annotations

from dataclasses import fields
from typing import TYPE_CHECKING, Any

from edify.elements.types.base import BaseElement
from edify.serialize.kinds import kind_for
from edify.serialize.version import SCHEMA_VERSION

if TYPE_CHECKING:
    from edify.builder.types.flags import Flags
    from edify.builder.types.state import BuilderState


def element_to_dict(element: BaseElement) -> dict[str, Any]:
    """Return the canonical dict representation of ``element``."""
    result: dict[str, Any] = {"kind": kind_for(type(element))}
    for spec in fields(element):
        raw_value = getattr(element, spec.name)
        result[spec.name] = _serialize_field_value(raw_value)
    return result


def _serialize_field_value(value: Any) -> Any:
    if isinstance(value, BaseElement):
        return element_to_dict(value)
    if isinstance(value, tuple):
        return [element_to_dict(child) for child in value]
    return value


def _flags_to_dict(flags: Flags) -> dict[str, bool]:
    return {spec.name: True for spec in fields(flags) if getattr(flags, spec.name)}


def state_to_dict(state: BuilderState) -> dict[str, Any]:
    """Return the canonical dict for a builder state (root element + flags)."""
    root_children = tuple(state.top_frame.children)
    from edify.elements.types.root import RootElement

    root_element = RootElement(children=root_children)
    document: dict[str, Any] = {
        "edify": SCHEMA_VERSION,
        "pattern": element_to_dict(root_element),
    }
    flag_map = _flags_to_dict(state.flags)
    if flag_map:
        document["flags"] = flag_map
    return document
