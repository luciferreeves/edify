"""Tests for the top-level :mod:`edify` package surface."""

import importlib.metadata

from edify import _resolve_installed_version


def test_version_falls_back_when_package_metadata_missing(monkeypatch):
    def raise_not_found(distribution_name: str) -> str:
        raise importlib.metadata.PackageNotFoundError(distribution_name)

    monkeypatch.setattr(importlib.metadata, "version", raise_not_found)
    assert _resolve_installed_version() == "0.0.0"
