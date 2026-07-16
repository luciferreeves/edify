"""Errors raised by the canonical (de)serializer through the public Pattern API."""

import json

import pytest

from edify import Pattern
from edify.errors.serialize import (
    IncompatibleSchemaVersionError,
    MissingSchemaKeyError,
    NonObjectJSONPayloadError,
    UnknownElementKindError,
)
from edify.serialize import JSONValue


def test_missing_edify_key_raises():
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict({"pattern": {"kind": "root", "children": []}})


def test_missing_pattern_key_raises():
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict({"edify": 0})


def test_missing_kind_on_nested_node_raises():
    document: dict[str, JSONValue] = {
        "edify": 0,
        "pattern": {"kind": "root", "children": [{"value": "x"}]},
    }
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict(document)


def test_incompatible_schema_version_raises():
    document: dict[str, JSONValue] = {"edify": 999, "pattern": {"kind": "root", "children": []}}
    with pytest.raises(IncompatibleSchemaVersionError):
        Pattern.from_dict(document)


def test_unknown_kind_raises():
    document: dict[str, JSONValue] = {
        "edify": 0,
        "pattern": {"kind": "root", "children": [{"kind": "mystery"}]},
    }
    with pytest.raises(UnknownElementKindError):
        Pattern.from_dict(document)


def test_bad_json_string_raises_decode_error():
    with pytest.raises(json.JSONDecodeError):
        Pattern.from_json("{not-valid-json}")


def test_non_object_json_payload_raises_non_object_json_payload_error():
    with pytest.raises(NonObjectJSONPayloadError, match="canonical JSON payload must be an object"):
        Pattern.from_json("[1, 2, 3]")


def test_incompatible_schema_version_with_composite_value_stringifies_it():
    document: dict[str, JSONValue] = {
        "edify": [1, 2, 3],
        "pattern": {"kind": "root", "children": []},
    }
    with pytest.raises(IncompatibleSchemaVersionError):
        Pattern.from_dict(document)


def test_pattern_key_not_a_root_element_produces_empty_pattern():
    document: dict[str, JSONValue] = {"edify": 0, "pattern": {"kind": "digit"}}
    restored = Pattern.from_dict(document)
    assert restored.to_regex_string() == "(?:)"
