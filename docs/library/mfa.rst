mfa
===

**Auth** · :doc:`Back to the library <index>`

A multi-factor authentication code.

.. code-block:: python

   from edify.library import mfa

   mfa('123456')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123456|2345678

   from edify.library import mfa
   mfa

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^\d{6,8}$

How it reads
------------

.. code-block:: text

   - The text must start with between 6 and 8 digits (0-9).

See the other validators in the :doc:`library <index>`.
