Product
=======

Every validator in the :doc:`product <../../library/product/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/product/index>`.

.. py:function:: edify.library.barcode(value: str) -> bool

   Barcode. See :doc:`../../library/product/barcode` for the full description.

   Emits ``^[A-Z0-9]{6,48}$``

.. py:function:: edify.library.gtin(value: str) -> bool

   GTIN. See :doc:`../../library/product/gtin` for the full description.

   Emits ``^(?:\d{8}|\d{12}|\d{13}|\d{14})$``

.. py:function:: edify.library.mpn(value: str) -> bool

   MPN. See :doc:`../../library/product/mpn` for the full description.

   Emits ``^[A-Z0-9][A-Z0-9\-_\.]{1,63}$``

