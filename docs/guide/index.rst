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
   :hidden:

   start/index
   builder/index
   atoms/index
   beyond/index

:doc:`Get started <start/index>`
--------------------------------

- :doc:`start/getting-started` — installing, a first pattern, and what ships in the
  box.
- :doc:`start/thinking-in-edify` — quantifiers come before the token, every builder
  is immutable, and patterns compare by what they emit.

:doc:`The builder <builder/index>`
----------------------------------

- :doc:`builder/anchors` — pinning a pattern to the start or end of the input.
- :doc:`builder/characters` — literals, ranges, and the named character classes.
- :doc:`builder/quantifiers` — repetition, including the lazy variants.
- :doc:`builder/groups` — grouping and alternation.
- :doc:`builder/captures` — keeping the text a group matched, and referring back.
- :doc:`builder/lookaround` — asserting what surrounds a position.
- :doc:`builder/flags` — case-insensitivity, dot-all, multiline, and verbose.

:doc:`Atoms <atoms/index>`
--------------------------

The 83 named fragments the :doc:`../library/index` validators are assembled from.

- :doc:`atoms/network` — addresses, hosts, ports, and their pieces.
- :doc:`atoms/numbers` — integers, decimals, bases, and money.
- :doc:`atoms/text` — characters, classes, and word shapes.
- :doc:`atoms/encodings` — base-N alphabets, hashes, and identifiers.
- :doc:`atoms/datetime` — date, time, and duration components.
- :doc:`atoms/web` — HTTP values, file names, and colours.
- :doc:`atoms/finance` — payment fragments and version numbers.
- :doc:`atoms/grouping` — bracket-delimited spans.

:doc:`Beyond the chain <beyond/index>`
--------------------------------------

- :doc:`beyond/composing` — reuse, operators, constants, and factory functions.
- :doc:`beyond/from-regex` — turning an existing regex string back into a chain.
- :doc:`beyond/matching` — running a compiled pattern against text.
- :doc:`beyond/errors` — the four-part diagnostics edify raises.
- :doc:`beyond/testing` — inline assertions and snapshot tests.
- :doc:`beyond/seeing` — explaining a pattern in prose or as a diagram.
- :doc:`beyond/serialization` — round-tripping a pattern through JSON.
- :doc:`beyond/integrations` — using a pattern as a framework validator.

For method signatures and parameter tables see the :doc:`../api/index`; for
ready-made validators you can call today, the :doc:`../library/index`.
