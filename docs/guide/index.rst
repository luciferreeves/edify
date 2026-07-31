Guide
=====

Edify builds regular expressions the way you'd describe them out loud. This guide
walks the whole surface from the ground up — every anchor, character class,
quantifier, group, and assertion — then the batteries around the builder: the atoms
the validators are made of, introspection, serialization, and framework
integrations.

Read it top to bottom the first time; each topic builds on the last. Come back to
any single page as a reference later.

.. toctree::
   :maxdepth: 2

   start/index
   builder/index
   atoms/index
   beyond/index

Where to start
--------------

- :doc:`start/index` — install it, build a first pattern, and learn the two rules
  that make the rest predictable.
- :doc:`builder/index` — the chain surface topic by topic: anchors, characters,
  quantifiers, groups, captures, lookaround, flags.
- :doc:`atoms/index` — the 83 named fragments the :doc:`../library/index`
  validators are assembled from.
- :doc:`beyond/index` — composing, matching, errors, testing, introspection,
  serialization, and integrations.

For method signatures and parameter tables see the :doc:`../api/index`; for
ready-made validators you can call today, the :doc:`../library/index`.
