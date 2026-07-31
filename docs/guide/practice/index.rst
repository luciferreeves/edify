In practice
===========

The rest of the guide covers what edify can express. This section covers what
happens when those patterns meet real input: text you did not write, in scripts you
did not anticipate, at volumes you do not control.

.. toctree::
   :hidden:

   recipes
   performance
   debugging
   unicode

- :doc:`recipes` — complete patterns for parsing, extracting, replacing, and
  splitting.
- :doc:`performance` — the pattern shape that causes catastrophic backtracking, and
  the build-time check that catches it.
- :doc:`debugging` — four ways to find out why a pattern does not match.
- :doc:`unicode` — which tokens reach beyond ASCII, and which quietly do not.
