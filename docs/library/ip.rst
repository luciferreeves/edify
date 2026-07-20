ip
==

**Address** · :doc:`Back to the library <index>`

An IP address, either IPv4 or IPv6.

.. code-block:: python

   from edify.library import ip

   ip('250.250.202.133')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 250.250.202.133|aA:A0a::

   from edify.library import ip
   ip

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}|(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?:(?::(?:[0-9a-fA-F]){1,4}){1,6})|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:]))|fe80:(?::(?:[0-9a-fA-F]){0,4}){0,4}%[0-9a-zA-Z]+|::(?:ffff(?::0{1,4})?:)?(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)|(?:(?:[0-9a-fA-F]){1,4}:){1,4}:(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)))$

See the other validators in the :doc:`library <index>`.
