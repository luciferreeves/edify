port
====

``port`` matches a TCP/UDP port number — a decimal integer from 0 to 65535, with
the upper bound enforced exactly rather than by digit count.

Under the hood it is an :func:`~edify.any_of` over range-anchored branches — one
for ``6553`` + ``0``–``5``, one for ``655`` + ``0``–``2`` + a digit, and so on down
to a lone digit — which together cover 0–65535 and nothing above it:

.. code-block:: python

   from edify import Pattern, any_of

   port = any_of(
       Pattern().start_of_input().string("6553").range("0", "5").end_of_input(),   # 65530–65535
       Pattern().start_of_input().string("655").range("0", "2").digit().end_of_input(),
       # … through …
       Pattern().start_of_input().range("1", "9").at_most(3).digit().end_of_input(),
       Pattern().start_of_input().char("0").end_of_input(),
   )

which emits:

.. code-block:: text

   (?:^6553[0-5]$|^655[0-2]\d$|^65[0-4]\d{2}$|^6[0-4]\d{3}$|^[1-5]\d{4}$|^[1-9]\d{0,3}$|^0$)

The full range, bounded exactly
-------------------------------

Any port in range, from the reserved low ports to the ephemeral high ones — and
because the value is range-checked, it stops precisely at 65535 rather than merely
allowing five digits:

.. code-block:: python

   port("0")       # True — the wildcard "any port"
   port("443")     # True — HTTPS
   port("8080")    # True
   port("65535")   # True — the maximum
   port("65536")   # False — one past the maximum
   port("99999")   # False — five digits, but out of range

.. edify-playground::
   :tests: 0|443|8080|65535|65536|99999

   from edify.library import port
   port

No sign, no decimal
-------------------

A port is a bare non-negative integer — no leading sign, no decimal point:

.. code-block:: python

   port("-1")    # False — no sign is allowed
   port("+80")   # False — no sign is allowed
   port("8.0")   # False — an integer, not a decimal
   port("abc")   # False — digits only

.. edify-playground::
   :tests: 80|-1|+80|8.0

   from edify.library import port
   port

Notes
-----

- To validate a whole ``host:port`` address rather than the port alone, use
  :doc:`socket`.
