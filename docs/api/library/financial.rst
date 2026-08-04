Finance
=======

Every validator in the :doc:`financial <../../library/financial/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/financial/index>`.

.. py:function:: edify.library.card(value: str) -> bool

   Card. See :doc:`../../library/financial/card` for the full description.

   Emits ``^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{1,7}$``

.. py:function:: edify.library.crypto(value: str) -> bool

   Crypto. See :doc:`../../library/financial/crypto` for the full description.

   Emits ``^[A-Z0-9]{3,10}$``

.. py:function:: edify.library.currency(value: str) -> bool

   Currency. See :doc:`../../library/financial/currency` for the full description.

   Emits ``^[A-Z]{3}$``

.. py:function:: edify.library.routing(value: str) -> bool

   Routing. See :doc:`../../library/financial/routing` for the full description.

   Emits ``^\d{9}$``

.. py:function:: edify.library.sortcode(value: str) -> bool

   Sort code. See :doc:`../../library/financial/sortcode` for the full description.

   Emits ``(?:^\d{2}\-\d{2}\-\d{2}$|^\d{6}$)``

.. py:function:: edify.library.vat(value: str) -> bool

   VAT. See :doc:`../../library/financial/vat` for the full description.

   Emits ``^[A-Z]{2}\d{6,12}$``

.. py:function:: edify.library.wallet(value: str) -> bool

   Wallet. See :doc:`../../library/financial/wallet` for the full description.

   Emits ``^(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-z0-9]{25,89}|0x[a-fA-F0-9]{40}|[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}|D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}|X[1-9A-HJ-NP-Za-km-z]{33})$``

