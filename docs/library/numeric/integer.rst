Integer
=======

**Integer** matches an `integer <https://en.wikipedia.org/wiki/Integer>`__ — a whole
number with an optional leading sign — the check for a
field holding a count, an offset, or an identifier that may be negative.

The construction is an :meth:`~edify.RegexBuilder.optional` sign class over ``+``
and ``-``, then :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit`, anchored end to end.

Signed and unsigned
-------------------

.. edify-playground::

   from edify.library import integer

   integer("42")     # unsigned
   integer("-42")    # negative
   integer("+42")    # an explicit plus
   integer("0")      # zero
   integer("007")    # leading zeros are accepted

Whole numbers only
------------------

A decimal point, a separator, or an exponent puts the value in another validator's
territory:

.. edify-playground::

   from edify.library import integer

   integer("42")      # whole
   integer("4.2")     # a decimal: see number
   integer("1,000")   # a thousands separator
   integer("1e5")     # an exponent: see scientific
   integer("")        # empty

Note that leading zeros pass, so ``007`` is accepted as the integer 7 — if the value
is really a zero-padded code, :doc:`../text/numeric` expresses that better. For
positive-only values see :doc:`natural`; for decimals, :doc:`number`.
