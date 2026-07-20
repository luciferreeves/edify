subnet
======

:doc:`Library <../index>` › :doc:`Address <index>` › **subnet**

``subnet`` matches a dotted-decimal IPv4 subnet mask — four octets, each a valid
mask byte (``255``, ``254``, ``252``, …, ``128``, ``0``).

.. code-block:: python

   from edify.library import subnet

   subnet("255.255.255.0")     # True
   subnet("255.255.0.0")       # True
   subnet("255.0.0.0")         # True
   subnet("255.255.255.1")     # False — 1 is not a mask byte
   subnet("192.168.0.0")       # False — those aren't mask bytes

What it matches
---------------

- Four dot-separated octets.
- Each octet is one of the **nine legal mask bytes**: ``255``, ``254``, ``252``,
  ``248``, ``240``, ``224``, ``192``, ``128``, or ``0``.
- Anchored at both ends.

It does **not** verify that the mask is *contiguous* (a well-formed netmask has
all its one-bits leading) — it checks each octet independently. For a network
block with a prefix length, see :doc:`cidr`.

Try it
------

.. edify-playground::
   :tests: 255.255.255.0|255.255.0.0|255.0.0.0|0.0.0.0|255.255.255.1|192.168.0.0

   from edify.library import subnet
   subnet

Pattern
-------

.. code-block:: text

   ^(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])\.(?:255|254|252|248|240|224|192|128|[0])$
