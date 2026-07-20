port
====

:doc:`Library <../index>` › :doc:`Address <index>` › **port**

``port`` matches a TCP/UDP port number — a decimal integer from 0 to 65535, with
the upper bound enforced exactly rather than by digit count.

.. code-block:: python

   from edify.library import port

   port("443")   # True

The full range 0–65535
----------------------

Any port in range, from the reserved low ports to the ephemeral high ones:

.. code-block:: python

   port("0")       # True — the wildcard "any port"
   port("80")      # True — HTTP
   port("443")     # True — HTTPS
   port("8080")    # True
   port("65535")   # True — the maximum

The upper boundary is exact
---------------------------

The pattern range-checks the value, so it stops precisely at 65535 — it does not
merely allow "up to five digits":

.. code-block:: python

   port("65535")   # True  — the largest legal port
   port("65536")   # False — one past the maximum
   port("99999")   # False — five digits, but out of range

What it rejects
---------------

.. code-block:: python

   port("-1")     # False — no sign is allowed
   port("+80")    # False — no sign is allowed
   port("abc")    # False — digits only
   port("8.0")    # False — an integer, not a decimal

To validate a whole ``host:port`` address rather than the port alone, use
:doc:`socket`.

Pattern
-------

.. code-block:: text

   (?:^6553[0-5]$|^655[0-2]\d$|^65[0-4]\d{2}$|^6[0-4]\d{3}$|^[1-5]\d{4}$|^[1-9]\d{0,3}$|^0$)
