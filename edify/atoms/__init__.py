"""Composable :class:`Pattern` atoms.

Each atom is an unanchored fragment meant to be spliced into a builder via
:meth:`edify.RegexBuilder.use` / :meth:`edify.Pattern.use`. Import any atom
directly from ``edify.atoms``.
"""

from edify.atoms.date_iso8601 import date_iso8601
from edify.atoms.domain_label import domain_label
from edify.atoms.email_local import email_local
from edify.atoms.hex_color import hex_color
from edify.atoms.hex_nibble import hex_nibble
from edify.atoms.hostname import hostname
from edify.atoms.ipv4_octet import ipv4_octet
from edify.atoms.port_number import port_number
from edify.atoms.semver import semver
from edify.atoms.slug import slug
from edify.atoms.time_24h import time_24h
from edify.atoms.username import username
from edify.atoms.uuid_v4 import uuid_v4

__all__ = [
    "date_iso8601",
    "domain_label",
    "email_local",
    "hex_color",
    "hex_nibble",
    "hostname",
    "ipv4_octet",
    "port_number",
    "semver",
    "slug",
    "time_24h",
    "username",
    "uuid_v4",
]
