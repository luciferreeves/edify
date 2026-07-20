port
====

:doc:`Library <../index>` › :doc:`Address <index>` › **port**

``port`` matches a TCP/UDP port number — an integer from 0 to 65535, with the
upper bound enforced exactly.

.. code-block:: python

   from edify.library import port

   port("80")       # True
   port("8080")     # True
   port("0")        # True
   port("65535")    # True — the maximum
   port("65536")    # False — above the maximum
   port("-1")       # False — no sign

What it matches
---------------

- A decimal integer **0–65535**, with the range enforced digit-by-digit
  (``65535`` matches, ``65536`` does not).
- No leading ``+`` or ``-`` sign, and no leading zeros beyond a lone ``0``.
- Anchored at both ends.

To validate a full ``host:port`` address, use :doc:`socket`.

Try it
------

.. edify-playground::
   :tests: 80|8080|443|0|65535|65536

   from edify.library import port
   port

Pattern
-------

.. code-block:: text

   (?:^6553[0-5]$|^655[0-2]\d$|^65[0-4]\d{2}$|^6[0-4]\d{3}$|^[1-5]\d{4}$|^[1-9]\d{0,3}$|^0$)
