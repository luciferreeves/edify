SEDOL
=====

A `SEDOL <https://en.wikipedia.org/wiki/SEDOL>`__ identifies a
security traded in the United Kingdom. It is seven characters: six from a restricted
alphabet, then a check digit. **SEDOL** matches that.

The construction is six characters from an :meth:`~edify.RegexBuilder.any_of` class
that **excludes vowels** — ``A``, ``E``, ``I``, ``O``, ``U`` are omitted so a SEDOL
can never spell a word — followed by a single :meth:`~edify.RegexBuilder.digit`.

Security identifiers
--------------------

.. edify-playground::

   from edify.library import sedol

   sedol("0263494")   # BAE Systems
   sedol("B1YW440")   # a modern SEDOL, letter-led
   sedol("3134865")

Vowels are excluded
-------------------

.. edify-playground::

   from edify.library import sedol

   sedol("B1YW440")   # valid characters
   sedol("BAYW440")   # A is a vowel
   sedol("B1YW44E")   # E is a vowel, and the last must be a digit
   sedol("B1YW44")    # six characters
   sedol("")          # empty

The seventh character is a weighted check digit that this cannot compute. SEDOLs
issued since 2004 begin with a letter and are assigned sequentially; older ones are
all digits. For the international wrapper see :doc:`isin`.
