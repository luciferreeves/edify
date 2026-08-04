Transport
=========

Every validator in the :doc:`transport <../../library/transport/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/transport/index>`.

.. py:function:: edify.library.aircraft(value: str) -> bool

   Aircraft. See :doc:`../../library/transport/aircraft` for the full description.

   Emits ``^[A-Z]{1,2}\-?[A-Z0-9]{1,5}$``

.. py:function:: edify.library.flight(value: str) -> bool

   Flight. See :doc:`../../library/transport/flight` for the full description.

   Emits ``^[A-Z]{2}\d{1,4}[A-Z]?$``

.. py:function:: edify.library.plate(value: str) -> bool

   Plate. See :doc:`../../library/transport/plate` for the full description.

   Emits ``^[A-Z0-9]{1,3}[- ]?[A-Z0-9]{1,4}$``

.. py:function:: edify.library.vehicle(value: str) -> bool

   Vehicle. See :doc:`../../library/transport/vehicle` for the full description.

   Emits ``^[A-Z0-9][A-Z0-9\- ]{3,17}$``

