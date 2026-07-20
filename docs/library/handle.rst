handle
======

**Contact** · :doc:`Back to the library <index>`

An ``@handle`` such as a social username.

.. code-block:: python

   from edify.library import handle

   handle('@jane')   # True
   handle('jane')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: @jane|@user_1|jane|@@

   from edify.library import handle
   handle

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^@[a-zA-Z0-9_]{1,30}$

How it reads
------------

.. code-block:: text

   - The text must start with "@".
   - Then the text must have between 1 and 30 of either one character from "a" through "z", one character from "A" through "Z", one character from "0" through "9", or "_".

See the other validators in the :doc:`library <index>`.
