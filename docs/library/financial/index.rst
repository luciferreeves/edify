Finance
=======

Payment instruments, bank routing identifiers, and currency codes. Each validator is
a callable :class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

A caveat that matters more here than anywhere else: several of these identifiers
carry **check digits** — a checksum built into the number that catches typos. A
regular expression cannot compute one, so a match means "the right shape", never
"a real account". Always run the checksum, and never treat a match as authorisation.

.. code-block:: python

   from edify.library import card, currency, vat

   card("4111 1111 1111 1111")   # True
   currency("USD")               # True
   vat("GB123456789")            # True

.. toctree::
   :hidden:

   card
   crypto
   currency
   routing
   sortcode
   vat
   wallet

Payment instruments
-------------------

- :doc:`card` — a payment card number.
- :doc:`wallet` — a cryptocurrency address; :doc:`crypto` — an asset ticker.

Bank routing
------------

- :doc:`routing` — a US routing number; :doc:`sortcode` — a UK sort code.

Codes
-----

- :doc:`currency` — an ISO 4217 currency code.
- :doc:`vat` — a European VAT registration number.
