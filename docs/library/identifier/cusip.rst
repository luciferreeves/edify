CUSIP
=====

A `CUSIP <https://www.cusip.com/>`__ identifies a North American security: six
characters for the issuer, two for the issue, and a check digit — nine in total.
**CUSIP** matches that length and alphabet.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(9)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase letters and digits.

Security identifiers
--------------------

.. edify-playground::

   from edify.library import cusip

   cusip("037833100")   # Apple
   cusip("38259P508")   # a CUSIP with a letter in the issue part
   cusip("594918104")   # Microsoft

Nine uppercase alphanumerics
----------------------------

.. edify-playground::

   from edify.library import cusip

   cusip("037833100")    # nine characters
   cusip("037833")       # six
   cusip("0378331000")   # ten
   cusip("037833a00")    # lowercase
   cusip("")             # empty

The ninth character is a modulo-10 check digit this cannot verify. Note also that the
letters ``I``, ``O``, and ``Z`` are excluded from CUSIPs to avoid confusion with
``1``, ``0``, and ``2``, and that exclusion is not enforced here. For the
international wrapper see :doc:`isin`; for the UK scheme, :doc:`sedol`.
