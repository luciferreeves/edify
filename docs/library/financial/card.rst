Card
====

**Card** matches a `payment card number <https://en.wikipedia.org/wiki/Payment_card_number>`__
as it is written on the card — four groups of digits, optionally separated by spaces
or hyphens, for a total of 13 to 19 digits.

The construction is three groups of :meth:`~edify.RegexBuilder.exactly`\ ``(4)``
:meth:`~edify.RegexBuilder.digit` separated by an
:meth:`~edify.RegexBuilder.optional` space or hyphen, then a final group of one to
seven digits — which is how the shorter and longer card lengths are covered.

Written forms
-------------

.. edify-playground::

   from edify.library import card

   card("4111111111111111")        # unseparated
   card("4111 1111 1111 1111")     # spaces, as printed on the card
   card("5500-0000-0000-0004")     # hyphens
   card("378282246310005")         # a 15-digit card

Digits and separators only
--------------------------

.. edify-playground::

   from edify.library import card

   card("4111111111111111")   # valid
   card("1234")               # too short
   card("4111 1111 1111 111a") # a letter
   card("")                   # empty

The critical limitation: card numbers carry a
`Luhn <https://en.wikipedia.org/wiki/Luhn_algorithm>`__ check digit, and this cannot
verify it — ``4111 1111 1111 1112`` matches and is not a valid number. Run the Luhn
check after matching, and remember that even a Luhn-valid number is not an authorised
one; only the payment processor can tell you that. Never log or store a full card
number.
