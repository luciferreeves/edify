Word
====

**Word** matches a run of `word characters <https://docs.python.org/3/library/re.html#index-32>`__
— letters, digits, and the underscore. It is the shape of a programming identifier
or a database column name, and the one character-class validator whose alphabet
extends past ASCII.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.word`, anchored end to end. Because the underlying class
is Unicode-aware by default, accented letters and other scripts count as word
characters too.

Identifier shapes
-----------------

.. edify-playground::

   from edify.library import word

   word("user_id")      # the classic identifier
   word("column2")      # digits are word characters
   word("_private")     # a leading underscore
   word("MAX_RETRIES")  # uppercase

Beyond ASCII
------------

This is where **Word** differs from :doc:`alphanumeric`: letters from any script
qualify, so a non-English identifier passes:

.. edify-playground::

   from edify.library import word

   word("naïve")     # an accented letter
   word("变量")       # a non-Latin script
   word("abc123")    # plain ASCII still works

Separators are excluded
-----------------------

Hyphens, dots, and spaces are not word characters:

.. edify-playground::

   from edify.library import word

   word("user_id")    # underscore joins
   word("user-id")    # hyphen: see slug
   word("user.id")    # a dot
   word("user id")    # a space
   word("")           # empty

For the ASCII-only variant see :doc:`alphanumeric`; for URL segments, :doc:`slug`.
