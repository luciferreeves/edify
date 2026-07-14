"""Errors raised by the canonical (de)serializer through the public Pattern API."""

import json

import pytest

from edify import Pattern
from edify.errors.serialize import (
    IncompatibleSchemaVersionError,
    MissingSchemaKeyError,
    UnknownElementKindError,
)


def test_missing_edify_key_raises():
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict({"pattern": {"kind": "root", "children": []}})


def test_missing_pattern_key_raises():
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict({"edify": 0})


def test_missing_kind_on_nested_node_raises():
    document = {
        "edify": 0,
        "pattern": {"kind": "root", "children": [{"value": "x"}]},
    }
    with pytest.raises(MissingSchemaKeyError):
        Pattern.from_dict(document)


def test_incompatible_schema_version_raises():
    document = {"edify": 999, "pattern": {"kind": "root", "children": []}}
    with pytest.raises(IncompatibleSchemaVersionError):
        Pattern.from_dict(document)


def test_unknown_kind_raises():
    document = {
        "edify": 0,
        "pattern": {"kind": "root", "children": [{"kind": "mystery"}]},
    }
    with pytest.raises(UnknownElementKindError):
        Pattern.from_dict(document)


def test_bad_json_string_raises_decode_error():
    with pytest.raises(json.JSONDecodeError):
        Pattern.from_json("{not-valid-json}")
