Constants
=========

Ready-made single-token :class:`~edify.Pattern` objects. Each is callable as a
one-character validator, composable with ``+`` and ``|``, and usable with
:meth:`~edify.RegexBuilder.use`.

.. code-block:: python

   from edify import DIGIT, LETTER, START, END

   DIGIT("5")                        # True
   (START + DIGIT + END).to_regex_string()   # '^\\d$'

Because every constant is a full :class:`~edify.Pattern`, the whole pattern
surface is available on it — :meth:`~edify.RegexBuilder.to_regex_string`,
:meth:`~edify.RegexBuilder.test`, the operators, and composition with
:meth:`~edify.RegexBuilder.use`.

Anchors
-------

Zero-width: each asserts a position without consuming a character.

.. py:data:: edify.START

   Emits ``^``. The start of the input, or of each line under
   :meth:`~edify.RegexBuilder.multi_line`. Equivalent to
   :meth:`~edify.RegexBuilder.start_of_input`.

.. py:data:: edify.END

   Emits ``$``. The end of the input, or of each line under
   :meth:`~edify.RegexBuilder.multi_line`. Equivalent to
   :meth:`~edify.RegexBuilder.end_of_input`.

.. py:data:: edify.WORD_BOUNDARY

   Emits ``\b``. The seam between a word character and a non-word character, or
   the edge of the string. Equivalent to
   :meth:`~edify.RegexBuilder.word_boundary`.

.. py:data:: edify.NON_WORD_BOUNDARY

   Emits ``\B``. Any position that is *not* a word boundary. Equivalent to
   :meth:`~edify.RegexBuilder.non_word_boundary`.

Character classes
-----------------

Each matches exactly one character.

.. py:data:: edify.DIGIT

   Emits ``\d``. One decimal digit in any script — Unicode-aware unless the
   pattern sets :meth:`~edify.RegexBuilder.ascii_only`. Equivalent to
   :meth:`~edify.RegexBuilder.digit`.

.. py:data:: edify.NON_DIGIT

   Emits ``\D``. One character that is not a decimal digit. Equivalent to
   :meth:`~edify.RegexBuilder.non_digit`.

.. py:data:: edify.WORD

   Emits ``\w``. One letter, digit, or underscore, in any script. Equivalent to
   :meth:`~edify.RegexBuilder.word`.

.. py:data:: edify.NON_WORD

   Emits ``\W``. One character that is not a word character. Equivalent to
   :meth:`~edify.RegexBuilder.non_word`.

.. py:data:: edify.WHITESPACE

   Emits ``\s``. One whitespace character. Equivalent to
   :meth:`~edify.RegexBuilder.whitespace_char`.

.. py:data:: edify.NON_WHITESPACE

   Emits ``\S``. One character that is not whitespace. Equivalent to
   :meth:`~edify.RegexBuilder.non_whitespace_char`.

.. py:data:: edify.ANY_CHAR

   Emits ``.``. Any one character **except** a newline, unless the pattern sets
   :meth:`~edify.RegexBuilder.dot_all`. Equivalent to
   :meth:`~edify.RegexBuilder.any_char`.

.. py:data:: edify.LETTER

   Emits ``[a-zA-Z]``. One ASCII letter — an explicit range, so it does not reach
   beyond ASCII the way ``WORD`` does. Equivalent to
   :meth:`~edify.RegexBuilder.letter`.

.. py:data:: edify.LOWERCASE

   Emits ``[a-z]``. One lowercase ASCII letter. Equivalent to
   :meth:`~edify.RegexBuilder.lowercase`.

.. py:data:: edify.UPPERCASE

   Emits ``[A-Z]``. One uppercase ASCII letter. Equivalent to
   :meth:`~edify.RegexBuilder.uppercase`.

.. py:data:: edify.ALPHANUMERIC

   Emits ``[a-zA-Z0-9]``. One ASCII letter or digit. Equivalent to
   :meth:`~edify.RegexBuilder.alphanumeric`.

Whitespace and control
----------------------

.. py:data:: edify.TAB

   Emits ``\t``. A horizontal tab. Equivalent to :meth:`~edify.RegexBuilder.tab`.

.. py:data:: edify.NEW_LINE

   Emits ``\n``. A line feed. Equivalent to
   :meth:`~edify.RegexBuilder.new_line`.

.. py:data:: edify.CARRIAGE_RETURN

   Emits ``\r``. A carriage return. Equivalent to
   :meth:`~edify.RegexBuilder.carriage_return`.

.. py:data:: edify.NULL_BYTE

   Emits ``\0``. A null character. Equivalent to
   :meth:`~edify.RegexBuilder.null_byte`.

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 34 24 42

   * - Constant
     - Emits
     - Matches
   * - :data:`~edify.START`
     - ``^``
     - start of input or line
   * - :data:`~edify.END`
     - ``$``
     - end of input or line
   * - :data:`~edify.WORD_BOUNDARY`
     - ``\b``
     - a word/non-word seam
   * - :data:`~edify.NON_WORD_BOUNDARY`
     - ``\B``
     - any non-seam position
   * - :data:`~edify.DIGIT`
     - ``\d``
     - one digit, any script
   * - :data:`~edify.NON_DIGIT`
     - ``\D``
     - one non-digit
   * - :data:`~edify.WORD`
     - ``\w``
     - one word character
   * - :data:`~edify.NON_WORD`
     - ``\W``
     - one non-word character
   * - :data:`~edify.WHITESPACE`
     - ``\s``
     - one whitespace character
   * - :data:`~edify.NON_WHITESPACE`
     - ``\S``
     - one non-whitespace character
   * - :data:`~edify.ANY_CHAR`
     - ``.``
     - any character but a newline
   * - :data:`~edify.LETTER`
     - ``[a-zA-Z]``
     - one ASCII letter
   * - :data:`~edify.LOWERCASE`
     - ``[a-z]``
     - one lowercase ASCII letter
   * - :data:`~edify.UPPERCASE`
     - ``[A-Z]``
     - one uppercase ASCII letter
   * - :data:`~edify.ALPHANUMERIC`
     - ``[a-zA-Z0-9]``
     - one ASCII letter or digit
   * - :data:`~edify.TAB`
     - ``\t``
     - a horizontal tab
   * - :data:`~edify.NEW_LINE`
     - ``\n``
     - a line feed
   * - :data:`~edify.CARRIAGE_RETURN`
     - ``\r``
     - a carriage return
   * - :data:`~edify.NULL_BYTE`
     - ``\0``
     - a null character
