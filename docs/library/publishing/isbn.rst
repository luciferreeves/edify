ISBN
====

An `ISBN <https://www.isbn-international.org/>`__ identifies a book edition. The
older form is 10 digits, the current one 13, and both may be written with hyphens or
spaces grouping the registrant elements. **ISBN** accepts both lengths and both
separators.

The two lengths are branches of an :func:`~edify.any_of`, each separately anchored:
nine digits with optional separators then a final character that may be ``X``, or
twelve digits then a final digit. The ``X`` exists because the ISBN-10 check digit is
computed modulo 11 and needs a symbol for the value ten.

Both lengths
------------

.. edify-playground::

   from edify.library import isbn

   isbn("978-3-16-148410-0")   # ISBN-13, hyphenated
   isbn("9783161484100")       # ISBN-13, bare
   isbn("0306406152")          # ISBN-10
   isbn("0-306-40615-2")       # ISBN-10, hyphenated
   isbn("978 3 16 148410 0")   # spaces instead of hyphens

The check character
-------------------

``X`` is valid only as the final character of an ISBN-10:

.. edify-playground::

   from edify.library import isbn

   isbn("080442957X")     # a valid ISBN-10 ending in X
   isbn("97831614841X0")  # X in the middle
   isbn("978316148410")   # twelve digits: neither length
   isbn("")               # empty

The check digit is *positional*, not arithmetic, here: this confirms an ``X`` sits
where one may sit but never computes the checksum, so ``0306406153`` matches and is
not a real ISBN. Run the modulo check before trusting one. For serials see
:doc:`issn`.
