otp
===

**Auth** · :doc:`Back to the library <index>`

A one-time passcode.

.. code-block:: python

   from edify.library import otp

   otp('123456')   # True
   otp('abc')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 123456|000000|abc|12

   from edify.library import otp
   otp

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^\d{6,8}$|^[A-Z0-9]{6,8}$)

How it reads
------------

.. code-block:: text

   - The text must contain either the very beginning of the text, then between 6 and 8 digits (0-9), then the very end of the text or the very beginning of the text, then between 6 and 8 of either one character from "A" through "Z" or one character from "0" through "9", then the very end of the text.

See the other validators in the :doc:`library <index>`.
