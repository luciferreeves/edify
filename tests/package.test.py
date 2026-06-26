"""Tests for the top-level :mod:`edify` package surface."""

import importlib
import importlib.metadata
import sys
from importlib.metadata import PackageNotFoundError


def test_version_falls_back_when_package_metadata_missing(monkeypatch):
    def raise_not_found(distribution_name: str) -> str:
        raise PackageNotFoundError(distribution_name)

    monkeypatch.setattr(importlib.metadata, "version", raise_not_found)
    sys.modules.pop("edify", None)
    reloaded_module = importlib.import_module("edify")
    assert reloaded_module.__version__ == "0.0.0"
