"""Deserialize a canonical dict back into a :class:`BuilderState`."""

from __future__ import annotations

from dataclasses import fields

from edify.builder.types.flags import Flags
from edify.builder.types.frame import StackFrame
from edify.builder.types.state import BuilderState
from edify.elements.types.base import BaseElement
from edify.elements.types.captures import CaptureElement, NamedCaptureElement
from edify.elements.types.leaves import EndOfInputElement, StartOfInputElement
from edify.elements.types.root import RootElement
from edify.elements.walk import walk_elements
from edify.errors.serialize import (
    IncompatibleSchemaVersionError,
    MissingSchemaKeyError,
    UnknownElementKindError,
)
from edify.serialize.kinds import class_for
from edify.serialize.types import JSONValue
from edify.serialize.version import SCHEMA_VERSION


def dict_to_element(tree: dict[str, JSONValue]) -> BaseElement:
    """Return the AST element described by ``tree``."""
    kind_value = tree.get("kind")
    if not isinstance(kind_value, str):
        raise MissingSchemaKeyError("kind")
    try:
        element_class = class_for(kind_value)
    except KeyError as reason:
        raise UnknownElementKindError(kind_value) from reason
    known_field_names = {spec.name for spec in fields(element_class)}
    constructor_kwargs: dict[str, BaseElement | tuple[BaseElement, ...] | JSONValue] = {}
    for name, raw_value in tree.items():
        if name == "kind":
            continue
        if name not in known_field_names:
            continue
        constructor_kwargs[name] = _deserialize_field_value(raw_value)
    return element_class(**constructor_kwargs)


def dict_to_state(document: dict[str, JSONValue]) -> BuilderState:
    """Return the :class:`BuilderState` described by ``document`` (canonical shape)."""
    _require_schema_version(document)
    pattern_tree = document.get("pattern")
    if not isinstance(pattern_tree, dict):
        raise MissingSchemaKeyError("pattern")
    root_element = dict_to_element(pattern_tree)
    root_children = _root_children(root_element)
    reconstructed_flags = _flags_from_document(document)
    named_groups = _collect_named_groups(root_children)
    total_captures = _count_capture_groups(root_children)
    start_indicators = [isinstance(child, StartOfInputElement) for child in root_children]
    end_indicators = [isinstance(child, EndOfInputElement) for child in root_children]
    has_start = any(start_indicators)
    has_end = any(end_indicators)
    root_frame = StackFrame(type_node=RootElement(), children=root_children)
    return BuilderState(
        has_defined_start=has_start,
        has_defined_end=has_end,
        flags=reconstructed_flags,
        stack=(root_frame,),
        named_groups=named_groups,
        total_capture_groups=total_captures,
    )


def _deserialize_field_value(
    value: JSONValue,
) -> BaseElement | tuple[BaseElement, ...] | JSONValue:
    if isinstance(value, list):
        element_items = [dict_to_element(item) for item in value if isinstance(item, dict)]
        return tuple(element_items)
    if isinstance(value, dict) and "kind" in value:
        return dict_to_element(value)
    return value


def _root_children(root_element: BaseElement) -> tuple[BaseElement, ...]:
    if isinstance(root_element, RootElement):
        return tuple(root_element.children)
    return ()


def _require_schema_version(document: dict[str, JSONValue]) -> None:
    if "edify" not in document:
        raise MissingSchemaKeyError("edify")
    seen_version = document["edify"]
    if seen_version == SCHEMA_VERSION:
        return
    if isinstance(seen_version, str | int | float | bool | type(None)):
        raise IncompatibleSchemaVersionError(seen_version, SCHEMA_VERSION)
    raise IncompatibleSchemaVersionError(repr(seen_version), SCHEMA_VERSION)


def _flags_from_document(document: dict[str, JSONValue]) -> Flags:
    raw_flag_map = document.get("flags")
    if not isinstance(raw_flag_map, dict):
        return Flags()
    flag_specs = fields(Flags)
    known_flag_names = {spec.name for spec in flag_specs}
    kwargs = {
        name: True for name, value in raw_flag_map.items() if name in known_flag_names and value
    }
    return Flags(**kwargs)


def _collect_named_groups(children: tuple[BaseElement, ...]) -> tuple[str, ...]:
    walked = walk_elements(children)
    named_group_names = [
        element.name for element in walked if isinstance(element, NamedCaptureElement)
    ]
    return tuple(named_group_names)


def _count_capture_groups(children: tuple[BaseElement, ...]) -> int:
    walked = walk_elements(children)
    capture_flags = [
        1 for element in walked if isinstance(element, CaptureElement | NamedCaptureElement)
    ]
    return sum(capture_flags)
