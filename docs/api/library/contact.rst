Contact
=======

Every validator in the :doc:`contact <../../library/contact/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/contact/index>`.

.. py:function:: edify.library.address(value: str) -> bool

   Address. See :doc:`../../library/contact/address` for the full description.

   Emits ``^\d+\s+(?:\s|[A-Za-z0-9.,'\-#/])+$``

.. py:function:: edify.library.email(value: str) -> bool

   Email. See :doc:`../../library/contact/email` for the full description.

   Emits ``^(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*@(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*|"(?:(?:[-\\-!#-[\]-]|\\[-\t\\-]))*")@(?:(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|[a-z0-9\-]*[a-z0-9]:(?:(?:[-\\-!-ZS-]|\\[-\t\\-]))+)\]))$``

.. py:function:: edify.library.email_rfc_5322(value: str) -> bool

   Email (RFC 5322). See :doc:`../../library/contact/email_rfc_5322` for the full description.

   Emits ``^(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*|"(?:(?:[-\\-!#-[\]-]|\\[-\t\\-]))*")@(?:(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|[a-z0-9\-]*[a-z0-9]:(?:(?:[-\\-!-ZS-]|\\[-\t\\-]))+)\])$``

.. py:function:: edify.library.fax(value: str) -> bool

   Fax. See :doc:`../../library/contact/fax` for the full description.

   Emits ``^\+?\d{1,4}?(?:\s|[\-\.])?\(?\d{1,3}?\)?(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,4}(?:\s|[\-\.])?\d{1,9}$``

.. py:function:: edify.library.handle(value: str) -> bool

   Handle. See :doc:`../../library/contact/handle` for the full description.

   Emits ``^@[a-zA-Z0-9_]{1,30}$``

.. py:function:: edify.library.pager(value: str) -> bool

   Pager. See :doc:`../../library/contact/pager` for the full description.

   Emits ``^\d{4,10}$``

.. py:function:: edify.library.phone(value: str) -> bool

   Phone. See :doc:`../../library/contact/phone` for the full description.

   Emits ``^(?:(?:(?:00|[\+])[ .-]?)?(?:\d{1,4}|\(\d{1,4}\))(?:[ .-]?(?:\d{1,4}|\(\d{1,4}\))){1,7}|\d{2,6})$``

.. py:function:: edify.library.username(value: str) -> bool

   Username. See :doc:`../../library/contact/username` for the full description.

   Emits ``^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,29}$``

