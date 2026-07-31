Currency
========

**Currency** matches an `ISO 4217 <https://www.iso.org/iso-4217-currency-codes.html>`__
currency code — three uppercase letters, ``USD``, ``EUR``, ``JPY``.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(3)``
:meth:`~edify.RegexBuilder.uppercase`, anchored end to end. Three letters, uppercase,
nothing else.

Currency codes
--------------

.. edify-playground::

   from edify.library import currency

   currency("USD")
   currency("EUR")
   currency("JPY")
   currency("XBT")   # an unofficial code still matches

Uppercase, exactly three
------------------------

.. edify-playground::

   from edify.library import currency

   currency("GBP")    # canonical
   currency("usd")    # lowercase
   currency("US")     # too short
   currency("USDT")   # four letters
   currency("$")      # a symbol, not a code

The pattern does not consult the ISO register, so any three uppercase letters pass —
``ZZZ`` matches. Check against the official list if the code must be real. Note also
that ISO 4217 defines the *number of decimal places* per currency, which is what you
need for amounts; the code alone does not carry it.
