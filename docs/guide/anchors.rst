Anchors
=======

Anchors don't match characters — they match *positions*. They pin the rest of
your pattern to the edges of the input or to the boundaries between words, so a
match has to land where you mean it to. Every anchor is **zero-width**: it
consumes no characters, it only asserts that the current position qualifies.

Start and end of input
-----------------------

:meth:`~edify.RegexBuilder.start_of_input` pins the pattern to the very
beginning of the string, and :meth:`~edify.RegexBuilder.end_of_input` to the
very end:

.. code-block:: python

   from edify import RegexBuilder

   RegexBuilder().start_of_input().digit().to_regex_string()   # '^\\d'
   RegexBuilder().digit().end_of_input().to_regex_string()     # '\\d$'

Use both to require that the *whole* string is the thing you described, not just
some slice of it:

.. code-block:: python

   year = RegexBuilder().start_of_input().exactly(4).digit().end_of_input().to_regex()

   year.match("2024")        # matches
   year.match("in 2024")     # no match — there is text before the digits
   year.match("2024 AD")     # no match — there is text after them

Without the anchors the same pattern would happily match the ``2024`` inside
``"in 2024 AD"``. Anchoring both ends is the difference between *"contains four
digits"* and *"is four digits."* Try it — only the bare four-digit strings match:

.. edify-playground::
   :tests: 2024|in 2024|2024 AD|abcd

   RegexBuilder() \
       .start_of_input() \
       .exactly(4).digit() \
       .end_of_input()

.. tip::

   :meth:`~edify.RegexBuilder.test` and :meth:`~edify.RegexBuilder.search` match
   *anywhere* in the string, so an unanchored pattern reports a hit on any
   substring. When you mean *"the whole string is this,"* anchor both ends — or
   compile and use ``fullmatch``, which requires the whole string on its own.
   Baking the anchors into the pattern keeps that intent attached to it wherever
   it travels.

Word boundaries
---------------

A word boundary is the seam between a word character (``\w`` — letters, digits,
underscore) and a non-word character (or the edge of the string).
:meth:`~edify.RegexBuilder.word_boundary` matches that seam;
:meth:`~edify.RegexBuilder.non_word_boundary` matches anywhere that *isn't* one:

.. code-block:: python

   RegexBuilder().word_boundary().word().word_boundary().to_regex_string()  # '\\b\\w\\b'
   RegexBuilder().non_word_boundary().to_regex_string()                     # '\\B'

Wrap a term in word boundaries to match it only as a whole word:

.. code-block:: python

   cat = (
       RegexBuilder()
       .word_boundary().string("cat").word_boundary()
       .to_regex()
   )

   cat.search("the cat sat")     # matches "cat"
   cat.search("concatenate")     # no match — "cat" here isn't a whole word

Like start and end of input, boundaries consume no characters — they only assert
that the position is (or isn't) on a word edge. Watch ``cat`` match as a whole
word but not inside ``concatenate`` or ``scatter``:

.. edify-playground::
   :tests: the cat sat|concatenate|a cat|scatter

   RegexBuilder() \
       .word_boundary() \
       .string("cat") \
       .word_boundary()

Anchor constants
----------------

Each anchor also exists as a ready-made, importable :class:`~edify.Pattern`
constant, so you can compose one without spelling out a builder. They emit
exactly what the methods do:

.. code-block:: python

   from edify import START, END, WORD_BOUNDARY, NON_WORD_BOUNDARY

   START.to_regex_string()             # '^'
   END.to_regex_string()               # '$'
   WORD_BOUNDARY.to_regex_string()     # '\\b'
   NON_WORD_BOUNDARY.to_regex_string() # '\\B'

Because a constant is a ``Pattern``, it composes with the ``+`` operator and
drops into any chain — a compact way to bracket an expression:

.. code-block:: python

   from edify import START, END, RegexBuilder

   (START + RegexBuilder().exactly(4).digit() + END).to_regex_string()   # '^\\d{4}$'

See :doc:`composing` for the full story on constants and operators.

Anchors and multiline
---------------------

By default ``^`` and ``$`` anchor to the ends of the *whole string*. Turn on the
:meth:`~edify.RegexBuilder.multi_line` flag and they anchor to the ends of every
*line* instead — so ``start_of_input`` matches just after each newline:

.. code-block:: python

   starts = (
       RegexBuilder().multi_line()
       .start_of_input().one_or_more().word()
       .to_regex()
   )
   [m.group() for m in starts.finditer("one\ntwo\nthree")]   # ['one', 'two', 'three']

Without ``multi_line`` that same pattern would only find ``'one'``. Flags are
covered in full on :doc:`flags`.

Quick reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 32 30 12 26

   * - Method
     - Constant
     - Emits
     - Matches at
   * - ``start_of_input()``
     - ``START``
     - ``^``
     - start of string (or line, with ``multi_line``)
   * - ``end_of_input()``
     - ``END``
     - ``$``
     - end of string (or line, with ``multi_line``)
   * - ``word_boundary()``
     - ``WORD_BOUNDARY``
     - ``\b``
     - a word/non-word seam
   * - ``non_word_boundary()``
     - ``NON_WORD_BOUNDARY``
     - ``\B``
     - any position that isn't a seam

Next
----

:doc:`characters` covers the tokens that actually match text — digits, letters,
whitespace, ranges, and character classes.
