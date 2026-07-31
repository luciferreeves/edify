Port
====

**Port** matches a TCP/UDP port number: an integer from 0 to 65535 (the range fixed by
:rfc:`6335`). The whole reason it is more than "one to five digits" is that the upper
bound is checked by *value*, not by digit count — it stops exactly at 65535.

There is no single quantifier for "≤ 65535", so edify spells it out as an
:func:`~edify.any_of` of range branches — ``6553`` + ``0``–``5``, then ``655`` +
``0``–``2`` + a digit, and so on down to a lone digit and ``0``, one branch per
digit-length, each capped at the right value.

The full range
--------------

Every port from the wildcard ``0``, through the reserved low ports, up to the
ephemeral high ones:

.. edify-playground::

   from edify.library import port

   port("0")       # "any port"
   port("80")      # HTTP
   port("443")     # HTTPS
   port("8080")    # a common alternate
   port("65535")   # the maximum

The boundary is exact
---------------------

``65535`` matches but ``65536`` does not, and a five-digit number out of range like
``99999`` is rejected too — the pattern knows the number, not just how many digits it
has:

.. edify-playground::

   from edify.library import port

   port("65535")   # the top of the range
   port("65536")   # one past the maximum
   port("70000")   # well past it
   port("99999")   # five digits, but out of range

No sign, no decimal
-------------------

A port is a bare non-negative integer, so a leading sign or a decimal point fails:

.. edify-playground::

   from edify.library import port

   port("22")    # a bare integer
   port("-1")    # no sign
   port("+80")   # no sign
   port("8.0")   # an integer, not a decimal

To validate a whole ``host:port`` address, use :doc:`socket`.
