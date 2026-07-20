hostname
========

:doc:`Library <../index>` › :doc:`Address <index>` › **hostname**

``hostname`` matches an RFC 1123 hostname — one or more dot-separated labels, with
the whole name capped at 253 characters. Unlike :doc:`domain`, a bare single
label such as ``localhost`` is valid.

.. code-block:: python

   from edify.library import hostname

   hostname("example.com")   # True
   hostname("localhost")     # True — a single label is fine
   hostname("host-1")        # True
   hostname("-bad")          # False — can't start with a hyphen
   hostname("a b")           # False — no spaces

What it matches
---------------

- **One or more labels** separated by dots; a single label alone is allowed.
- Each label is 1–63 characters of letters, digits, and interior hyphens.
- A leading length check caps the **whole name at 1–253 characters**.
- Anchored at both ends.

Unlike :doc:`domain` it does not require a letters-only TLD, so ``host-1`` and
``localhost`` match. For a ``host:port`` pair use :doc:`socket`.

Try it
------

.. edify-playground::
   :tests: example.com|localhost|host-1|db.internal|-bad|a b

   from edify.library import hostname
   hostname

Pattern
-------

.. code-block:: text

   ^(?=.{1,253}$)(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$
