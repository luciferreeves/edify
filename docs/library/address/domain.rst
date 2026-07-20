domain
======

:doc:`Library <../index>` › :doc:`Address <index>` › **domain**

``domain`` matches a DNS domain name — one or more dot-separated labels ending in
a letters-only top-level domain.

.. code-block:: python

   from edify.library import domain

   domain("example.com")      # True
   domain("sub.example.io")   # True
   domain("a.co")             # True
   domain("example")          # False — no TLD
   domain("-bad.com")         # False — a label can't start with a hyphen

What it matches
---------------

- **One or more labels**, each 1–63 characters of letters, digits, and interior
  hyphens (a label may not start or end with a hyphen).
- A trailing **TLD of 2–63 letters** (see :doc:`tld`).
- Anchored at both ends.

For a name that may be a bare single label (like ``localhost``) use
:doc:`hostname`; for one label on its own use :doc:`subdomain`.

Try it
------

.. edify-playground::
   :tests: example.com|sub.example.io|a.co|my-site.org|example|-bad.com

   from edify.library import domain
   domain

Pattern
-------

.. code-block:: text

   ^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}$
