Alpha
=====

**Alpha** matches a non-empty run of
`ASCII <https://en.wikipedia.org/wiki/ASCII>`__ letters and nothing else — the check
behind a "letters only" form field. It is the narrowest of the character-class
validators: no digits, no spaces, no punctuation.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.letter`, anchored between
:meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input` so the whole string must qualify.

Letters in either case
----------------------

.. edify-playground::

   from edify.library import alpha

   alpha("Hello")     # mixed case
   alpha("abc")       # lowercase
   alpha("ABC")       # uppercase
   alpha("a")         # a single letter

Nothing else
------------

Digits, spaces, punctuation, and the empty string all fail — including the accented
letters that a "letters only" field usually ought to accept:

.. edify-playground::

   from edify.library import alpha

   alpha("Hello")     # letters
   alpha("Hello1")    # a digit
   alpha("Hello ")    # a trailing space
   alpha("héllo")     # é is not an ASCII letter
   alpha("")          # empty

The ASCII-only range is the important caveat: real names contain accents, and
rejecting them is a common source of exclusion. Reach for :doc:`script` or
:doc:`unicode` when the field holds names. For letters and digits together see
:doc:`alphanumeric`.
