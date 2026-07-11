"""Tests for the top-level :mod:`edify` package surface."""

import importlib
import importlib.metadata

import edify


def test_version_falls_back_when_package_metadata_missing(monkeypatch):
    def raise_not_found(distribution_name: str) -> str:
        raise importlib.metadata.PackageNotFoundError(distribution_name)

    monkeypatch.setattr(importlib.metadata, "version", raise_not_found)
    reloaded = importlib.reload(edify)
    assert reloaded.__version__ == "0.0.0"
