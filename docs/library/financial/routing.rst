Routing
=======

An `ABA routing number <https://en.wikipedia.org/wiki/ABA_routing_transit_number>`__
identifies a US financial institution for transfers and direct deposits. It is
exactly nine digits, and **Routing** matches that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(9)``
:meth:`~edify.RegexBuilder.digit`, anchored end to end.

Nine digits
-----------

.. edify-playground::

   from edify.library import routing

   routing("021000021")   # a real bank's routing number
   routing("011000015")
   routing("000000000")   # shape-valid, not a real institution

Exactly nine, digits only
-------------------------

.. edify-playground::

   from edify.library import routing

   routing("021000021")    # nine digits
   routing("12345")        # too few
   routing("0210000211")   # too many
   routing("02100002a")    # a letter
   routing("")             # empty

Routing numbers carry a weighted check digit that this cannot verify — ``000000000``
matches and is not valid. Compute the checksum, and confirm the institution exists
before moving money. The shape is identical to some other nine-digit identifiers, so
context decides what a number means. For the UK equivalent see :doc:`sortcode`.
