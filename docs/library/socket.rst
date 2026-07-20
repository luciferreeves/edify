socket
======

**Address** · :doc:`Back to the library <index>`

A ``host:port`` socket address.

.. code-block:: python

   from edify.library import socket

   socket('250.250.202.133:1')   # True

Edit the string, or the pattern itself:

.. edify-playground::
   :tests: 250.250.202.133:1|[aA:0]:23

   from edify.library import socket
   socket

Pattern
-------

The regex this validator emits:

.. code-block:: text

   ^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}|\[[0-9a-fA-F:]+\]|[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*):\d{1,5}$

See the other validators in the :doc:`library <index>`.
