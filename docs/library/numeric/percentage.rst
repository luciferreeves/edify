Percentage
==========

**Percentage** matches a `percentage <https://en.wikipedia.org/wiki/Percentage>`__ —
a number, optionally negative and optionally fractional, followed by a ``%`` sign.
An optional space before the sign is allowed, since both spacings are common in
written text.

The construction is an :meth:`~edify.RegexBuilder.optional` ``-``, digits, an
optional fractional part, an optional :meth:`~edify.RegexBuilder.whitespace_char`,
then the literal ``%``.

Written percentages
-------------------

.. edify-playground::

   from edify.library import percentage

   percentage("50%")      # a whole percentage
   percentage("99.9%")    # fractional
   percentage("100%")     # the usual maximum
   percentage("0%")       # zero
   percentage("50 %")     # a space before the sign

Values outside 0–100
--------------------

The range is not capped, because percentages legitimately exceed 100 (growth) and go
below zero (decline):

.. edify-playground::

   from edify.library import percentage

   percentage("150%")    # growth above 100
   percentage("-25%")    # a decline
   percentage("1000%")   # any magnitude

The sign is required
--------------------

Without ``%`` it is just a number:

.. edify-playground::

   from edify.library import percentage

   percentage("50%")    # with the sign
   percentage("50")     # a bare number: see number
   percentage("%50")    # the sign leads
   percentage("")       # empty

A plus sign is not accepted, so ``+5%`` fails — normalise it away first. For the bare
value see :doc:`number`; for the ``a:b`` comparison form, :doc:`ratio`.
