ASIN
====

An `ASIN <https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number>`__
identifies a product in Amazon's catalogue. It is ten uppercase alphanumeric
characters, and **ASIN** matches that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(10)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase letters and digits.

Product identifiers
-------------------

.. edify-playground::

   from edify.library import asin

   asin("B08N5WRWNW")   # a typical product ASIN
   asin("B00005N5PF")
   asin("0306406152")   # a book ASIN matches its ISBN-10

Ten uppercase alphanumerics
---------------------------

.. edify-playground::

   from edify.library import asin

   asin("B08N5WRWNW")    # ten characters
   asin("b08n5wrwnw")    # lowercase
   asin("B08N5WRWN")     # nine
   asin("B08N5WRWNWX")   # eleven
   asin("")              # empty

Two things to note. For books the ASIN *is* the ISBN-10, so the same string may be
valid under :doc:`../publishing/isbn` — which also means this shape overlaps with
:doc:`cusip`-adjacent identifiers of similar width. And an ASIN is marketplace-scoped:
the same product can carry different ASINs in different regions.
