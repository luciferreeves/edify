ipv6
====

**Address** · :doc:`Back to the library <index>`

An IPv6 address in its standard hexadecimal form.

.. code-block:: python

   from edify.library import ipv6

   ipv6('2001:db8::1')   # True
   ipv6('1.2.3.4')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 2001:db8::1|::1|fe80::1|1.2.3.4|xyz

   from edify.library import ipv6
   ipv6

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:(?:[0-9a-fA-F]){1,4}:){7}(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,7}:|(?:(?:[0-9a-fA-F]){1,4}:){1,6}:(?:[0-9a-fA-F]){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,5}(?::(?:[0-9a-fA-F]){1,4}){1,2}|(?:(?:[0-9a-fA-F]){1,4}:){1,4}(?::(?:[0-9a-fA-F]){1,4}){1,3}|(?:(?:[0-9a-fA-F]){1,4}:){1,3}(?::(?:[0-9a-fA-F]){1,4}){1,4}|(?:(?:[0-9a-fA-F]){1,4}:){1,2}(?::(?:[0-9a-fA-F]){1,4}){1,5}|(?:[0-9a-fA-F]){1,4}:(?:(?::(?:[0-9a-fA-F]){1,4}){1,6})|:(?:(?:(?::(?:[0-9a-fA-F]){1,4}){1,7}|[:]))|fe80:(?::(?:[0-9a-fA-F]){0,4}){0,4}%[0-9a-zA-Z]+|::(?:ffff(?::0{1,4})?:)?(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)|(?:(?:[0-9a-fA-F]){1,4}:){1,4}:(?:(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d)\.){3}(?:25[0-5]|(?:(?:2[0-4]|1?\d))?\d))$

See the other validators in the :doc:`library <index>`.
