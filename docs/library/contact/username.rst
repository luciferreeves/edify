Username
========

**Username** matches an
`account name <https://en.wikipedia.org/wiki/User_(computing)>`__ in the
shape most services settle on: it starts
with a letter or digit, then allows letters, digits, underscore, dot, and hyphen, for
a total length of 3 to 30 characters.

The construction is a leading :meth:`~edify.RegexBuilder.alphanumeric`, then
:meth:`~edify.RegexBuilder.between`\ ``(2, 29)`` of an
:meth:`~edify.RegexBuilder.any_of` class adding the three separators. Requiring the
first character to be alphanumeric is what keeps a name from beginning with
punctuation.

Accepted names
--------------

.. edify-playground::

   from edify.library import username

   username("alice")       # letters
   username("user_name")   # an underscore
   username("a.b-c")       # a dot and a hyphen
   username("user2024")    # digits
   username("abc")         # the three-character minimum

The first character
-------------------

Punctuation may appear inside a name but never at the start:

.. edify-playground::

   from edify.library import username

   username("_private")   # leading underscore
   username(".hidden")    # leading dot
   username("-dash")      # leading hyphen
   username("a_private")  # fine once a letter leads

Length bounds
-------------

Three characters is the floor and thirty the ceiling — the range most platforms use:

.. edify-playground::

   from edify.library import username

   username("abc")        # at the minimum
   username("ab")         # too short
   username("x" * 30)     # at the maximum
   username("x" * 31)     # too long
   username("has space")  # spaces are not allowed

Shape is only half the problem: names that differ by look-alike characters, or by
case alone, can be used for impersonation. Normalise case, check
:doc:`../text/script` for mixed-script spoofing, and enforce uniqueness on the
normalised form. For the public ``@``-prefixed form see :doc:`handle`.
