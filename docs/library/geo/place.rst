Place
=====

**Place** matches the name of a `settlement <https://en.wikipedia.org/wiki/Populated_place>`__
or region as it is written on a form — a letter-led string that may contain spaces
and the punctuation place names use.

The construction is a leading :meth:`~edify.RegexBuilder.letter`, then
:meth:`~edify.RegexBuilder.between`\ ``(1, 99)`` over an
:meth:`~edify.RegexBuilder.any_of` class of letters, spaces, ``.``, ``,``, ``'``, and
``-``.

Place names
-----------

.. edify-playground::

   from edify.library import place

   place("New York")
   place("Paris")
   place("St. Louis")            # a full stop
   place("Stratford-upon-Avon")  # hyphens
   place("King's Lynn")          # an apostrophe

Letters and place punctuation
-----------------------------

.. edify-playground::

   from edify.library import place

   place("Springfield")   # valid
   place("12345")         # digits
   place("2nd City")      # must start with a letter
   place("")              # empty

The important limitation: the character class is ASCII letters only, so ``München``,
``São Paulo``, and every name in a non-Latin script are rejected — which makes this
unsuitable as the sole validator for an international address form. Use
:doc:`../text/printable` or :doc:`../text/script` where names may be non-English, and
never reject a user's real place name on the strength of a pattern.
