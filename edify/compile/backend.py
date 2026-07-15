"""Engine backends for compiling a rendered pattern string.

The stdlib :mod:`re` backend is always available. The third-party ``regex``
module is loaded lazily so ``import edify`` never imports it. Callers that
select ``engine="regex"`` reach this module and receive a clean
:class:`edify.errors.backend.MissingRegexBackendError` when the extra is
not installed.
"""

from __future__ import annotations

import re
from importlib import import_module
from types import ModuleType
from typing import cast

from edify.builder.types.engine import Engine
from edify.builder.types.flags import Flags
from edify.errors.backend import MissingRegexBackendError, VariableWidthLookbehindNotSupportedError


def load_regex_module() -> ModuleType:
    """Return the third-party ``regex`` module, importing it on first call.

    Raises:
        MissingRegexBackendError: when the ``regex`` extra is not installed.
    """
    try:
        return import_module("regex")
    except ImportError as reason:
        raise MissingRegexBackendError() from reason


def compile_pattern(pattern: str, engine: Engine, flags: Flags) -> re.Pattern[str]:
    """Compile ``pattern`` with the selected engine, applying ``flags`` as a bitmask.

    The return type is declared as :class:`re.Pattern` so downstream call sites
    stay strongly typed. Under ``engine="regex"`` the value is a ``regex.Pattern``
    that mirrors :class:`re.Pattern`'s method surface.

    Raises:
        VariableWidthLookbehindNotSupportedError: when ``engine='re'`` and the
            pattern uses a variable-width lookbehind body that stdlib re rejects.
        MissingRegexBackendError: when ``engine='regex'`` and the ``regex`` module
            is not installed.
    """
    if engine == "regex":
        regex_module = load_regex_module()
        return cast(
            re.Pattern[str], regex_module.compile(pattern, _regex_flag_bitmask(regex_module, flags))
        )
    try:
        return re.compile(pattern, flags=_re_flag_bitmask(flags))
    except re.error as reason:
        if "look-behind" in str(reason):
            raise VariableWidthLookbehindNotSupportedError() from reason
        raise


def _re_flag_bitmask(flags: Flags) -> int:
    bitmask = 0
    if flags.ascii_only:
        bitmask = bitmask | re.A
    if flags.debug:
        bitmask = bitmask | re.DEBUG
    if flags.ignore_case:
        bitmask = bitmask | re.I
    if flags.multiline:
        bitmask = bitmask | re.M
    if flags.dotall:
        bitmask = bitmask | re.S
    if flags.verbose:
        bitmask = bitmask | re.X
    return bitmask


def _regex_flag_bitmask(regex_module: ModuleType, flags: Flags) -> int:
    bitmask = 0
    if flags.ascii_only:
        bitmask = bitmask | regex_module.A
    if flags.debug:
        bitmask = bitmask | regex_module.DEBUG
    if flags.ignore_case:
        bitmask = bitmask | regex_module.I
    if flags.multiline:
        bitmask = bitmask | regex_module.M
    if flags.dotall:
        bitmask = bitmask | regex_module.S
    if flags.verbose:
        bitmask = bitmask | regex_module.X
    return bitmask
