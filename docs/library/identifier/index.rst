Identifiers
===========

The largest category: identifiers from finance, telecoms, government, shipping, and
the web. Each validator is a callable :class:`~edify.Pattern`: import it, call it
with a string, get a ``bool``.

Many of these carry **check digits** — a checksum built into the value that catches
transcription errors. A pattern cannot compute one, so a match means "the right
shape" and never "a real, issued identifier". Where a checksum exists, each page says
so.

.. code-block:: python

   from edify.library import uuid, iban, imei

   uuid("550e8400-e29b-41d4-a716-446655440000")   # True
   iban("GB82WEST12345698765432")                 # True
   imei("490154203237518")                        # True

.. toctree::
   :hidden:

   arn
   asin
   bic
   cusip
   did
   ein
   guid
   iata
   iban
   icao
   iccid
   imei
   imo
   isin
   itin
   lei
   mac
   meid
   mmsi
   orcid
   sedol
   sku
   ssn
   tin
   uuid
   vin

Universal identifiers
---------------------

- :doc:`uuid` — a version-checked UUID; :doc:`guid` — the brace-wrapped variant.
- :doc:`did` — a decentralised identifier; :doc:`arn` — a cloud resource name.

Finance and securities
----------------------

- :doc:`iban` — an international bank account number; :doc:`bic` — a bank code.
- :doc:`isin`, :doc:`cusip`, :doc:`sedol` — securities identifiers.
- :doc:`lei` — a legal entity identifier.

Government and tax
------------------

- :doc:`ssn` — a US social security number; :doc:`itin` — its taxpayer counterpart.
- :doc:`ein` — an employer identification number; :doc:`tin` — either form.

Devices and networks
--------------------

- :doc:`mac` — a hardware address; :doc:`imei` and :doc:`meid` — mobile devices.
- :doc:`iccid` — a SIM card identifier.

Transport and trade
-------------------

- :doc:`iata` and :doc:`icao` — airline and airport codes.
- :doc:`imo` and :doc:`mmsi` — ship identifiers.
- :doc:`asin` and :doc:`sku` — retail item identifiers.
- :doc:`vin` — a vehicle identification number.

People
------

- :doc:`orcid` — a researcher identifier.
