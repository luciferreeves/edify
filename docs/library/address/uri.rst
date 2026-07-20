uri
===

:doc:`Library <../index>` › :doc:`Address <index>` › **uri**

``uri`` matches the generic URI shape — a scheme, a colon, and a non-empty
opaque-or-path remainder. It accepts *any* scheme, not just HTTP.

.. code-block:: python

   from edify.library import uri

   uri("https://example.com")   # True
   uri("mailto:a@b.com")        # True
   uri("urn:isbn:0451450523")   # True
   uri("no scheme")             # False — no scheme + colon

What it matches
---------------

- A **scheme** starting with a letter, then any of letters, digits, ``+``, ``.``,
  ``-``.
- A ``:`` followed by **one or more non-whitespace characters**.
- Anchored at both ends.

Because it accepts any scheme, ``mailto:``, ``urn:``, ``ftp:``, ``tel:`` and
friends all match. For the narrower HTTP/HTTPS web-URL shape (with an optional
scheme and a validated TLD), use :doc:`url`.

Try it
------

.. edify-playground::
   :tests: https://example.com|mailto:a@b.com|urn:isbn:0451450523|ftp://host/f|no scheme

   from edify.library import uri
   uri

Pattern
-------

.. code-block:: text

   ^[a-zA-Z][a-zA-Z0-9\+\.\-]*:\S+$
