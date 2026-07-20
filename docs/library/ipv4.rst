ipv4
====

**Address** · :doc:`Back to the library <index>`

An IPv4 address in dotted-decimal form.

.. code-block:: python

   from edify.library import ipv4

   ipv4('192.168.0.1')   # True
   ipv4('999.1.1.1')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 192.168.0.1|10.0.0.255|8.8.8.8|999.1.1.1|1.2.3

   from edify.library import ipv4
   ipv4

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$

See the other validators in the :doc:`library <index>`.
