subnet
======

:doc:`Library <../index>` › :doc:`Address <index>` › **subnet**

``subnet`` matches a dotted-decimal IPv4 subnet mask — four octets, each one of
the nine byte values a mask can legally take.

.. code-block:: python

   from edify.library import subnet

   subnet("255.255.255.0")   # True

The nine mask bytes
-------------------

A mask byte is a run of one-bits followed by zero-bits, which leaves exactly nine
possibilities: ``255``, ``254``, ``252``, ``248``, ``240``, ``224``, ``192``,
``128``, and ``0``. ``subnet`` checks each octet against that set:

.. code-block:: python

   subnet("255.255.255.0")     # True — a /24
   subnet("255.255.0.0")       # True — a /16
   subnet("255.0.0.0")         # True — an /8
   subnet("255.255.255.128")   # True — a /25 (128 is a legal mask byte)
   subnet("0.0.0.0")           # True — the all-zero mask

What it rejects
---------------

Any octet outside the nine mask bytes fails, so ordinary addresses do not pass:

.. code-block:: python

   subnet("255.255.255.1")   # False — 1 is not a mask byte
   subnet("192.168.0.0")     # False — 192 is a mask byte, but 168 is not
   subnet("255.255.255")     # False — only three octets

.. note::

   ``subnet`` validates each octet **independently**; it does not check that the
   mask is *contiguous* (all one-bits leading). A discontiguous but
   byte-legal mask like ``255.0.255.0`` matches even though it is not a valid
   netmask. For a network block with a prefix length instead, use :doc:`cidr`.

Pattern
-------

.. code-block:: text

   ^(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])$
