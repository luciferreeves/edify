port
====

``port`` matches a TCP/UDP port number: an integer from 0 to 65535. The whole
reason it is more than ``\d{1,5}`` is that the upper bound is checked by *value*,
not by digit count — it stops exactly at 65535.

.. edify-playground::
   :tests: 0|80|443|8080|65535|65536|99999|-1|+80|8.0

   from edify.library import port
   port

**The full range.** Every port from the wildcard ``0`` through the reserved low
ports and up to the ephemeral high ones:

.. code-block:: python

   port("0")       # True — "any port"
   port("80")      # True — HTTP
   port("443")     # True — HTTPS
   port("65535")   # True — the maximum

**The boundary is exact.** ``65535`` matches but ``65536`` does not, and a
five-digit number out of range like ``99999`` is rejected too — the pattern knows
the number, not just how many digits it has:

.. code-block:: python

   port("65535")   # True
   port("65536")   # False — one past the maximum
   port("99999")   # False — five digits, but out of range

**No sign, no decimal.** A port is a bare non-negative integer:

.. code-block:: python

   port("-1")    # False — no sign
   port("+80")   # False — no sign
   port("8.0")   # False — an integer, not a decimal

There is no single quantifier for "≤ 65535", so edify spells it out as an
:func:`~edify.any_of` of range branches — ``6553`` + ``0``–``5``, ``655`` +
``0``–``2`` + a digit, and so on down to a lone digit, one branch per digit-length.
To validate a whole ``host:port`` address, use :doc:`socket`.
