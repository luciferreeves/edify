"""Escape user-provided string fragments for safe insertion into a regex pattern.

Two different escape scopes:

* :func:`escape_special` — for literals that will land *outside* a character
  class (``.string()``, ``.char()``, ``.anything_but_string()``). Every regex
  metacharacter must be escaped because the fragment is embedded directly
  into the concatenation stream.
* :func:`escape_for_char_class` — for literals that will land *inside*
  ``[...]``. Only ``\\``, ``]``, ``^`` (first position), and ``-``
  (interior position) need escaping; everything else is a literal inside a
  class. This is the minimal correct form.
"""

from __future__ import annotations

import re

_CHAR_CLASS_ESCAPE_ALWAYS = {"\\", "]"}
_RANGE_BOUND_ESCAPE = {"\\", "]", "^", "-"}


def escape_special(value: str) -> str:
    """Return ``value`` with all regex metacharacters backslash-escaped.

    Args:
        value: A literal fragment supplied by the user.

    Returns:
        The fragment with every regex metacharacter escaped, safe to embed
        directly into a compiled pattern.
    """
    return re.escape(value)


def escape_range_bound(character: str) -> str:
    """Return ``character`` escaped for use as a ``[a-z]`` range endpoint.

    A range endpoint carries syntactic weight wherever it lands in the class, so
    the position-sensitive rules of :func:`escape_for_char_class` do not apply:
    ``]`` would close the class, ``^`` would negate it, ``-`` would be read as a
    range operator, and ``\\`` would escape whatever follows.

    Args:
        character: A single range endpoint supplied by the user.

    Returns:
        The endpoint, backslash-escaped when it would otherwise be syntactic.
    """
    if character in _RANGE_BOUND_ESCAPE:
        return "\\" + character
    return character


def escape_for_char_class(characters: str) -> str:
    """Return ``characters`` escaped for insertion inside ``[...]``.

    Escapes exactly the characters that would otherwise carry syntactic
    meaning inside a character class:

    * ``\\`` and ``]`` — always.
    * ``^`` — only at position 0 (else the whole class would negate).
    * ``-`` — only in interior position (position 0 and the final position
      are unambiguously literal).

    Every other character passes through untouched.

    Args:
        characters: The raw class body supplied by the user.

    Returns:
        The escaped fragment, safe to place between ``[`` and ``]``.
    """
    if characters == "":
        return characters
    last_index = len(characters) - 1
    escaped_pieces: list[str] = []
    for position, character in enumerate(characters):
        if character in _CHAR_CLASS_ESCAPE_ALWAYS:
            escaped_pieces.append("\\" + character)
            continue
        if character == "^" and position == 0:
            escaped_pieces.append("\\^")
            continue
        if character == "-" and 0 < position < last_index:
            escaped_pieces.append("\\-")
            continue
        escaped_pieces.append(character)
    return "".join(escaped_pieces)
