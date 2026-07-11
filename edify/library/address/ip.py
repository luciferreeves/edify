"""``ip`` — IPv4 or IPv6 address shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

_IPV4_OCTET = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)"
_IPV4 = rf"{_IPV4_OCTET}\.{_IPV4_OCTET}\.{_IPV4_OCTET}\.{_IPV4_OCTET}"

_IPV6 = (
    r"(?:"
    r"([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}"
    r"|([0-9a-fA-F]{1,4}:){1,7}:"
    r"|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}"
    r"|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}"
    r"|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}"
    r"|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}"
    r"|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}"
    r"|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})"
    r"|:((:[0-9a-fA-F]{1,4}){1,7}|:)"
    r"|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}"
    r"|::(ffff(:0{1,4}){0,1}:){0,1}"
    r"((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}"
    r"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"
    r"|([0-9a-fA-F]{1,4}:){1,4}:"
    r"((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}"
    r"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"
    r")"
)

ip = RegexBackedPattern(rf"^(?:{_IPV4}|{_IPV6})$")
"""Callable :class:`Pattern` for IPv4 dotted-quad or any IPv6 form."""
