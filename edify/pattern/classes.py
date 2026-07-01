"""Pre-built :class:`Pattern` constants for the built-in character classes.

Import these instead of writing ``Pattern().digit()`` etc. Every constant
is a fresh singleton :class:`Pattern` instance with a single element in
its root frame; combining them via the operator algebra
(``DIGIT + WORD`` etc.) leaves the constants themselves untouched.

The lowercase :func:`~edify.pattern.factories.values.string`,
:func:`~edify.pattern.factories.values.char` and friends live in
:mod:`edify.pattern.factories.values`.
"""

from __future__ import annotations

from edify.pattern.composition import Pattern

ANY_CHAR: Pattern = Pattern().any_char()
WHITESPACE: Pattern = Pattern().whitespace_char()
NON_WHITESPACE: Pattern = Pattern().non_whitespace_char()
DIGIT: Pattern = Pattern().digit()
NON_DIGIT: Pattern = Pattern().non_digit()
WORD: Pattern = Pattern().word()
NON_WORD: Pattern = Pattern().non_word()
NEW_LINE: Pattern = Pattern().new_line()
CARRIAGE_RETURN: Pattern = Pattern().carriage_return()
TAB: Pattern = Pattern().tab()
NULL_BYTE: Pattern = Pattern().null_byte()
LETTER: Pattern = Pattern().letter()
UPPERCASE: Pattern = Pattern().uppercase()
LOWERCASE: Pattern = Pattern().lowercase()
ALPHANUMERIC: Pattern = Pattern().alphanumeric()
