cidr
====

**Address** · :doc:`Back to the library <index>`

A CIDR network block such as ``10.0.0.0/8``.

.. code-block:: python

   from edify.library import cidr

   cidr('10.0.0.0/8')   # True
   cidr('10.0.0.0')   # False

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 10.0.0.0/8|192.168.1.0/24|10.0.0.0

   from edify.library import cidr
   cidr

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}/(?:3[0-2]|[12]?\d)|(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}/(?:12[0-8]|1[01]\d|[1-9]?\d))$

See the other validators in the :doc:`library <index>`.
