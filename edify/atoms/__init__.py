"""Composable :class:`Pattern` atoms.

Each atom is an unanchored fragment meant to be spliced into a builder via
:meth:`edify.RegexBuilder.use` / :meth:`edify.Pattern.use`. Import any atom
directly from ``edify.atoms``.
"""

from edify.atoms.clock import clock
from edify.atoms.hexcolor import hexcolor
from edify.atoms.hostname import hostname
from edify.atoms.isodate import isodate
from edify.atoms.label import label
from edify.atoms.localpart import localpart
from edify.atoms.nibble import nibble
from edify.atoms.octet import octet
from edify.atoms.port import port
from edify.atoms.semver import semver
from edify.atoms.slug import slug
from edify.atoms.username import username
from edify.atoms.uuid import uuid

__all__ = [
    "clock",
    "hexcolor",
    "hostname",
    "isodate",
    "label",
    "localpart",
    "nibble",
    "octet",
    "port",
    "semver",
    "slug",
    "username",
    "uuid",
]
