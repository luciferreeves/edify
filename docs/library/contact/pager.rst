Pager
=====

A `pager <https://en.wikipedia.org/wiki/Pager>`__ code is the short numeric string
sent to a paging device — still in daily use in hospitals and emergency services,
where reliability matters more than features. **Pager** matches 4 to 10 digits.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(4, 10)`` over
:meth:`~edify.RegexBuilder.digit`, anchored end to end. There are no separators: a
pager code is dialled as one run.

Code lengths
------------

.. edify-playground::

   from edify.library import pager

   pager("1234")         # a four-digit internal code
   pager("12345")        # five digits
   pager("5551234567")   # a full ten-digit number

Digits only, within range
-------------------------

.. edify-playground::

   from edify.library import pager

   pager("12345")         # in range
   pager("123")           # too short
   pager("12345678901")   # too long
   pager("555-1234")      # separators are not part of a code
   pager("")              # empty

For a full telephone number with country codes and separators see :doc:`phone`.
