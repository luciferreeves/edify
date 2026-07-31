MPN
===

A `manufacturer part number <https://en.wikipedia.org/wiki/Part_number>`__ is the
reference a manufacturer assigns to a component. There is no standard — each
manufacturer invents its own scheme — so **MPN** matches the shape they share: an
uppercase alphanumeric run with the separators parts commonly use.

The construction is a leading uppercase alphanumeric, then
:meth:`~edify.RegexBuilder.between`\ ``(1, 63)`` over an
:meth:`~edify.RegexBuilder.any_of` class adding ``-``, ``_``, and ``.``.

Part numbers
------------

.. edify-playground::

   from edify.library import mpn

   mpn("ABC-123")
   mpn("XYZ_9")
   mpn("LM317T")
   mpn("STM32F103C8T6")
   mpn("2N3904")
   mpn("RC0603FR-071KL")   # a passive component reference

Uppercase, alphanumeric-led
---------------------------

.. edify-playground::

   from edify.library import mpn

   mpn("ABC-123")   # valid
   mpn("abc-123")   # lowercase
   mpn("-ABC123")   # must start alphanumeric
   mpn("A")         # too short
   mpn("")          # empty

Because there is no standard, a match tells you a string *could* be a part number and
nothing more — the same part often has different numbers at different distributors,
and MPNs are not unique across manufacturers. Pair one with the manufacturer name to
identify a part. For the trade item number see :doc:`gtin`.
