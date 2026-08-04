Identifiers
===========

Every validator in the :doc:`identifier <../../library/identifier/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/identifier/index>`.

.. py:function:: edify.library.arn(value: str) -> bool

   ARN. See :doc:`../../library/identifier/arn` for the full description.

   Emits ``^arn:[a-z\-]+:[a-z0-9\-]+:[a-z0-9\-]*:\d*:.+$``

.. py:function:: edify.library.asin(value: str) -> bool

   ASIN. See :doc:`../../library/identifier/asin` for the full description.

   Emits ``^[A-Z0-9]{10}$``

.. py:function:: edify.library.bic(value: str) -> bool

   BIC. See :doc:`../../library/identifier/bic` for the full description.

   Emits ``^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}(?:[A-Z0-9]{3})?$``

.. py:function:: edify.library.cusip(value: str) -> bool

   CUSIP. See :doc:`../../library/identifier/cusip` for the full description.

   Emits ``^[A-Z0-9]{9}$``

.. py:function:: edify.library.did(value: str) -> bool

   DID. See :doc:`../../library/identifier/did` for the full description.

   Emits ``^did:[a-z0-9]+:.+$``

.. py:function:: edify.library.ein(value: str) -> bool

   EIN. See :doc:`../../library/identifier/ein` for the full description.

   Emits ``^\d{2}\-\d{7}$``

.. py:function:: edify.library.guid(value: str) -> bool

   GUID. See :doc:`../../library/identifier/guid` for the full description.

   Emits ``^\{?[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}\}?$``

.. py:function:: edify.library.iata(value: str) -> bool

   IATA. See :doc:`../../library/identifier/iata` for the full description.

   Emits ``^[A-Z]{2,3}$``

.. py:function:: edify.library.iban(value: str) -> bool

   IBAN. See :doc:`../../library/identifier/iban` for the full description.

   Emits ``^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$``

.. py:function:: edify.library.icao(value: str) -> bool

   ICAO. See :doc:`../../library/identifier/icao` for the full description.

   Emits ``^[A-Z]{3,4}$``

.. py:function:: edify.library.iccid(value: str) -> bool

   ICCID. See :doc:`../../library/identifier/iccid` for the full description.

   Emits ``^\d{19,22}$``

.. py:function:: edify.library.imei(value: str) -> bool

   IMEI. See :doc:`../../library/identifier/imei` for the full description.

   Emits ``^\d{15}$``

.. py:function:: edify.library.imo(value: str) -> bool

   IMO. See :doc:`../../library/identifier/imo` for the full description.

   Emits ``^IMO\d{7}$``

.. py:function:: edify.library.isin(value: str) -> bool

   ISIN. See :doc:`../../library/identifier/isin` for the full description.

   Emits ``^[A-Z]{2}[A-Z0-9]{9}\d$``

.. py:function:: edify.library.itin(value: str) -> bool

   ITIN. See :doc:`../../library/identifier/itin` for the full description.

   Emits ``^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$``

.. py:function:: edify.library.lei(value: str) -> bool

   LEI. See :doc:`../../library/identifier/lei` for the full description.

   Emits ``^[A-Z0-9]{20}$``

.. py:function:: edify.library.mac(value: str) -> bool

   MAC. See :doc:`../../library/identifier/mac` for the full description.

   Emits ``^(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$``

.. py:function:: edify.library.meid(value: str) -> bool

   MEID. See :doc:`../../library/identifier/meid` for the full description.

   Emits ``^[0-9A-F]{14}$``

.. py:function:: edify.library.mmsi(value: str) -> bool

   MMSI. See :doc:`../../library/identifier/mmsi` for the full description.

   Emits ``^\d{9}$``

.. py:function:: edify.library.orcid(value: str) -> bool

   ORCID. See :doc:`../../library/identifier/orcid` for the full description.

   Emits ``^\d{4}\-\d{4}\-\d{4}\-\d{3}(?:\d|[X])$``

.. py:function:: edify.library.sedol(value: str) -> bool

   SEDOL. See :doc:`../../library/identifier/sedol` for the full description.

   Emits ``^[B-DF-HJ-NP-TV-XY-Z0-9]{6}\d$``

.. py:function:: edify.library.sku(value: str) -> bool

   SKU. See :doc:`../../library/identifier/sku` for the full description.

   Emits ``^[A-Za-z0-9-_./]{4,20}$``

.. py:function:: edify.library.ssn(value: str) -> bool

   SSN. See :doc:`../../library/identifier/ssn` for the full description.

   Emits ``^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$``

.. py:function:: edify.library.tin(value: str) -> bool

   TIN. See :doc:`../../library/identifier/tin` for the full description.

   Emits ``(?:^(?!(?:666|000|9\d{2}))\d{3}\-(?!00)\d{2}\-(?!0{4})\d{4}$|^\d{2}\-\d{7}$|^9\d{2}\-(?:5\d|6[0-5]|7\d|8[0-8]|9[0-2]|9[4-9])\-\d{4}$)``

.. py:function:: edify.library.uuid(value: str) -> bool

   UUID. See :doc:`../../library/identifier/uuid` for the full description.

   Emits ``^[0-9a-f]{8}\-[0-9a-f]{4}\-[0-5][0-9a-f]{3}\-[089ab][0-9a-f]{3}\-[0-9a-f]{12}$``

.. py:function:: edify.library.vin(value: str) -> bool

   VIN. See :doc:`../../library/identifier/vin` for the full description.

   Emits ``^[A-HJ-NPR-Z0-9]{17}$``

