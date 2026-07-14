"""``protocol`` — common network protocol name."""

from __future__ import annotations

from edify import Pattern, any_of

protocol = any_of(
    Pattern().string("https"),
    Pattern().string("http"),
    Pattern().string("ftps"),
    Pattern().string("ftp"),
    Pattern().string("wss"),
    Pattern().string("ws"),
    Pattern().string("ssh"),
    Pattern().string("git"),
    Pattern().string("file"),
)
"""Composable :class:`Pattern` fragment for a common protocol name."""
