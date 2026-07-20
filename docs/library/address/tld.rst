tld
===

:doc:`Library <../index>` › :doc:`Address <index>` › **tld**

``tld`` matches a top-level domain — 2 to 63 letters, like ``com``, ``io``, or
``museum``. It is the trailing component :doc:`domain` requires.

.. code-block:: python

   from edify.library import tld

   tld("com")      # True
   tld("io")       # True
   tld("museum")   # True
   tld("c")        # False — too short (minimum two letters)
   tld("123")      # False — letters only

What it matches
---------------

- **2–63 letters**, upper or lower case.
- No digits, hyphens, or dots — the leading dot of ``.com`` is not part of the
  TLD itself.
- Anchored at both ends.

It matches the *shape* of a TLD, not the IANA registry — ``zzz`` matches even
though it is not a real TLD.

Try it
------

.. edify-playground::
   :tests: com|io|museum|dev|c|123

   from edify.library import tld
   tld

Pattern
-------

.. code-block:: text

   ^[a-zA-Z]{2,63}$
