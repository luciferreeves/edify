port
====

**Address** · :doc:`Back to the library <index>`

A TCP/UDP port number (0–65535).

.. code-block:: python

   from edify.library import port

   port('8080')   # True
   port('70000')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 8080|443|0|70000|abc

   from edify.library import port
   port

Pattern
-------

The regex this validator emits:

.. code-block:: text

   (?:^6553[0-5]$|^655[0-2]\d$|^65[0-4]\d{2}$|^6[0-4]\d{3}$|^[1-5]\d{4}$|^[1-9]\d{0,3}$|^0$)

See the other validators in the :doc:`library <index>`.
