subdomain
=========

:doc:`Library <../index>` › :doc:`Address <index>` › **subdomain**

``subdomain`` matches a single DNS label — the ``api`` in ``api.example.com`` — 2
to 63 characters, alphanumeric with optional interior hyphens.

.. code-block:: python

   from edify.library import subdomain

   subdomain("api")      # True
   subdomain("my-sub")   # True
   subdomain("a1")       # True
   subdomain("-bad")     # False — can't start with a hyphen
   subdomain("a b")      # False — no spaces or dots

What it matches
---------------

- A **single label** of 2–63 characters.
- Letters, digits, and **interior** hyphens only — the first and last character
  must be alphanumeric.
- No dots (it is one label, not a dotted name).
- Anchored at both ends.

For a full dotted name use :doc:`domain` or :doc:`hostname`.

Try it
------

.. edify-playground::
   :tests: api|my-sub|a1|staging-2|-bad|a b

   from edify.library import subdomain
   subdomain

Pattern
-------

.. code-block:: text

   ^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$
