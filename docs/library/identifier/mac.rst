MAC
===

A `MAC address <https://en.wikipedia.org/wiki/MAC_address>`__ identifies a network
interface: six bytes written as hex pairs, separated by colons or hyphens.
**MAC** matches both separator styles, in either case.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(5)`` groups of two hex
digits plus a separator from an :meth:`~edify.RegexBuilder.any_of_chars` set of ``:``
and ``-``, then a final pair.

Both separators
---------------

.. edify-playground::

   from edify.library import mac

   mac("00:1A:2B:3C:4D:5E")   # colon separated
   mac("00-1A-2B-3C-4D-5E")   # hyphen separated
   mac("00:1a:2b:3c:4d:5e")   # lowercase hex
   mac("FF:FF:FF:FF:FF:FF")   # the broadcast address

Six pairs, consistently separated
---------------------------------

.. edify-playground::

   from edify.library import mac

   mac("00:1A:2B:3C:4D:5E")   # six pairs
   mac("001A2B3C4D5E")        # no separators
   mac("00:1A:2B:3C:4D")      # five pairs
   mac("0:1A:2B:3C:4D:5E")    # a single-digit group
   mac("")                     # empty

The dotted Cisco notation ``001a.2b3c.4d5e`` is not matched. Note also that a MAC
address is not a reliable identity: it is trivially spoofed, and modern devices
randomise it for privacy — so never use one for authentication or long-term
tracking. For network addresses see :doc:`../address/ip`.
