Medical
=======

Every validator in the :doc:`medical <../../library/medical/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/medical/index>`.

.. py:function:: edify.library.blood(value: str) -> bool

   Blood. See :doc:`../../library/medical/blood` for the full description.

   Emits ``^(?:(?:AB|[ABO]))[+-]$``

.. py:function:: edify.library.dicom(value: str) -> bool

   DICOM. See :doc:`../../library/medical/dicom` for the full description.

   Emits ``^\d+(?:\.\d+)+$``

.. py:function:: edify.library.dosage(value: str) -> bool

   Dosage. See :doc:`../../library/medical/dosage` for the full description.

   Emits ``^\d+(?:\.\d+)?\s?(?:mg|kg|ml|mcg|iu|[gl])(?:/(?:kg|day|dose))?$``

.. py:function:: edify.library.medical(value: str) -> bool

   Medical code. See :doc:`../../library/medical/medical` for the full description.

   Emits ``^(?:\d{6,18}|[A-TV-Z]\d[A-Z0-9](?:\.[A-Z0-9]{1,4})?|\d{10}|\d{1,7}\-\d)$``

