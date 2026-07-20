port
====

A TCP/UDP port is an integer from 0 to 65535. The interesting part is the upper
bound: ``port`` checks the *value*, not the digit count, so it stops precisely at
65535 — ``65536`` and ``99999`` are both five digits, and both are rejected.

.. edify-playground::
   :tests: 0|443|8080|65535|65536|99999|-1|8.0

   from edify.library import port
   port

There is no way to say "a number ≤ 65535" with a single quantifier, so edify
spells it out as an :func:`~edify.any_of` of range branches — ``6553`` + ``0``–``5``,
``655`` + ``0``–``2`` + a digit, and so on down to a lone digit — one branch per
digit-length, each capped at the right value. A leading sign or a decimal point
fails; it is a bare non-negative integer. To validate a whole ``host:port``
address, use :doc:`socket`.
