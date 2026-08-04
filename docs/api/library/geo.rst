Geo
===

Every validator in the :doc:`geo <../../library/geo/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/geo/index>`.

.. py:function:: edify.library.altitude(value: str) -> bool

   Altitude. See :doc:`../../library/geo/altitude` for the full description.

   Emits ``^\-?\d+(?:\.\d+)?\s?(?:ft|km|mi|[m])?$``

.. py:function:: edify.library.bearing(value: str) -> bool

   Bearing. See :doc:`../../library/geo/bearing` for the full description.

   Emits ``^(?:360(?:\.0+)?|(?:3[0-5]\d|[1-2]\d\d|\d{1,2})(?:\.\d+)?)°?$``

.. py:function:: edify.library.coordinate(value: str) -> bool

   Coordinate. See :doc:`../../library/geo/coordinate` for the full description.

   Emits ``^\-?(?:90(?:\.0+)?|[0-8]?\d(?:\.\d+)?)\s*,\s*\-?(?:180(?:\.0+)?|(?:1[0-7]\d|[0-9]?\d)(?:\.\d+)?)$``

.. py:function:: edify.library.geohash(value: str) -> bool

   Geohash. See :doc:`../../library/geo/geohash` for the full description.

   Emits ``^[0-9bcdefghjkmnpqrstuvwxyz]{1,12}$``

.. py:function:: edify.library.mgrs(value: str) -> bool

   MGRS. See :doc:`../../library/geo/mgrs` for the full description.

   Emits ``^\d{1,2}[C-HJ-NP-X][A-Z]{2}(?:\d{2}|\d{4}|\d{6}|\d{8}|\d{10})$``

.. py:function:: edify.library.place(value: str) -> bool

   Place. See :doc:`../../library/geo/place` for the full description.

   Emits ``^[a-zA-Z][A-Za-z \.,'\-]{1,99}$``

.. py:function:: edify.library.plus(value: str) -> bool

   Plus code. See :doc:`../../library/geo/plus` for the full description.

   Emits ``^[23456789CFGHJMPQRVWX]{2,8}\+[23456789CFGHJMPQRVWX]{2,3}(?:\s+.+)?$``

.. py:function:: edify.library.postal(value: str) -> bool

   Postal. See :doc:`../../library/geo/postal` for the full description.

   Emits ``^(?:(?:(?:120|122))\d{2}|(?:NL\-)?\d{4}\s*[A-Z]{2}|(?:(?:[AC-FHKNPRTV-Y]\d{2}|D6W))[ -]?[0-9AC-FHKNPRTV-Y]{4}|(?:GIR 0AA|(?:[A-Za-z]\d{1,2}|[A-Za-z][A-HJ-Ya-hj-y]\d{1,2}|[A-Za-z]\d[A-Za-z]|[A-Za-z][A-HJ-Ya-hj-y]\d(?:[A-Za-z])?)\s?\d(?:[A-Za-z]){2})|96950|971\d{2}|972\d{2}|973\d{2}|974\d{2}|976\d{2}|980\d{2}|987\d{2}|988\d{2}|AI\-2640|BB\d{5}|FIQQ 1ZZ|GX11 1AA|LT\-\d{5}|LV\-\d{4}|MD\-?\d{4}|MSR \d{4}|STHL 1ZZ|TKCA 1ZZ|VC\d{4}|VG\d{4}|WS\d{4}|\d{2}\-\d{3}|\d{3}\s\d{2}|\d{3}|\d{3}(?:\-\d{2})?|\d{3}\-\d{4}|\d{4}\s\d{4}|\d{4}|\d{4}(?:\-[A-Z])?|\d{4}\-\d{3}|\d{5}|\d{5}(?:\-\d{4})?|\d{5}\-\d{3}|(?:\d{5}|\d{7})|\d{6}|\d{7}|[A-Z]\d[A-Z]\s?\d[A-Z]\d|[A-Z]\d{3}|[A-Z]\d{4}[A-Z]{3}|[A-Z]{2}\s\d{5}|[A-Z]{2}\d\-\d{4}|[A-Z]{2}\d{2}\s\d{3}|[A-Z]{2}\d{2}|[A-Z]{2}\d{4}|[A-Z]{3}\s\d{4}|\d{5}(?:[-](?:\s|[\-])\d{4})?|(?!0)\d{6})$``

