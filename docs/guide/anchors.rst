Anchors
=======

Anchors don't match characters — they match *positions*. They pin the rest of
your pattern to the edges of the input or to the boundaries between words, so a
match has to land where you mean it to.

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
digits"* and *"is four digits."*

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
that the position is (or isn't) on a word edge.

Next
----

:doc:`characters` covers the tokens that actually match text — digits, letters,
whitespace, ranges, and character classes.
