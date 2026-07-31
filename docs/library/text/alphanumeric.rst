Alphanumeric
============

**Alphanumeric** matches a non-empty run of
`ASCII <https://en.wikipedia.org/wiki/ASCII>`__ letters and digits — the check
behind a field that allows names and numbers but no punctuation, spaces, or
symbols.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.alphanumeric`, anchored between
:meth:`~edify.RegexBuilder.start_of_input` and
:meth:`~edify.RegexBuilder.end_of_input`, so a single stray character anywhere
fails the whole string.

Letters and digits together
---------------------------

.. edify-playground::

   from edify.library import alphanumeric

   alphanumeric("abc123")   # both classes
   alphanumeric("Hello")    # letters alone
   alphanumeric("2024")     # digits alone
   alphanumeric("a1")       # the shortest mix

Nothing else
------------

Separators and symbols fall outside, which is what distinguishes this from
:doc:`word` and :doc:`slug`:

.. edify-playground::

   from edify.library import alphanumeric

   alphanumeric("abc123")    # valid
   alphanumeric("abc_123")   # underscore: see word
   alphanumeric("abc-123")   # hyphen: see slug
   alphanumeric("abc 123")   # a space
   alphanumeric("")          # empty

Like :doc:`alpha` this is ASCII-only, so accented letters are rejected — reach for
:doc:`unicode` or :doc:`script` when the field holds names. For the underscore
variant see :doc:`word`.
