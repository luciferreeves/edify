"""Serialize a :class:`Pattern` into the canonical dict form."""

from __future__ import annotations

from dataclasses import fields

from edify.builder.types.flags import Flags
from edify.builder.types.state import BuilderState
from edify.elements.types.base import BaseElement
from edify.elements.types.root import RootElement
from edify.serialize.kinds import kind_for
from edify.serialize.types import JSONValue
from edify.serialize.version import SCHEMA_VERSION

_ElementFieldValue = BaseElement | tuple[BaseElement, ...] | str | int


def element_to_dict(element: BaseElement) -> dict[str, JSONValue]:
    """Return the canonical dict representation of ``element``."""
    result: dict[str, JSONValue] = {"kind": kind_for(type(element))}
    for spec in fields(element):
        raw_value = getattr(element, spec.name)
        result[spec.name] = _serialize_field_value(raw_value)
    return result


def state_to_dict(state: BuilderState) -> dict[str, JSONValue]:
    """Return the canonical dict for a builder state (root element + flags)."""
    root_children = tuple(state.top_frame.children)
    root_element = RootElement(children=root_children)
    root_dict = element_to_dict(root_element)
    document: dict[str, JSONValue] = {
        "edify": SCHEMA_VERSION,
        "pattern": root_dict,
    }
    flag_map = _flags_to_dict(state.flags)
    if flag_map:
        document["flags"] = flag_map
    return document


def _serialize_field_value(value: _ElementFieldValue) -> JSONValue:
    if isinstance(value, BaseElement):
        return element_to_dict(value)
    if isinstance(value, tuple):
        return [element_to_dict(child) for child in value]
    if isinstance(value, str):
        return value
    return value


def _flags_to_dict(flags: Flags) -> dict[str, JSONValue]:
    return {spec.name: True for spec in fields(flags) if getattr(flags, spec.name)}
