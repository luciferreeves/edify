email_rfc_5322
==============

**Contact** · :doc:`Back to the library <index>`

An email address validated against the RFC 5322 grammar.

.. code-block:: python

   from edify.library import email_rfc_5322

   email_rfc_5322('user@example.com')   # True
   email_rfc_5322('not-an-email')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: user@example.com|a.b@test.co|not-an-email|@no.com

   from edify.library import email_rfc_5322
   email_rfc_5322

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+(?:\.(?:[a-z0-9!\#\$%\&'\*\+/=\?\^_`\{\|\}\~\-])+)*|"(?:(?:[\x01-\x08\\v\\f\x0e-\x1f!#-[]-]|\\[\x01-\t\\v\\f\x0e-]))*")@(?:(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|[a-z0-9\-]*[a-z0-9]:(?:(?:[\x01-\x08\\v\\f\x0e-\x1f!-ZS-]|\\[\x01-\t\\v\\f\x0e-]))+)\])$

See the other validators in the :doc:`library <index>`.
