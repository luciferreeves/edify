Library
=======

The signature index for all 228 ready-made validators in :mod:`edify.library`,
grouped by category. Every one has the same shape:

.. code-block:: python

   from edify.library import uuid

   uuid("550e8400-e29b-41d4-a716-446655440000")   # True
   uuid("nope")                                   # False

Each is a callable :class:`~edify.Pattern`, so alongside calling it you can emit its
regex with :meth:`~edify.RegexBuilder.to_regex_string`, compile it with
:meth:`~edify.RegexBuilder.to_regex`, or embed it in a larger chain with
:meth:`~edify.RegexBuilder.use`.

This section lists what each validator emits. For what it accepts and rejects, the
reasoning behind the pattern, and runnable examples, use the
:doc:`../../library/index` instead — every entry here links to its page there.

.. toctree::
   :hidden:

   address
   api
   auth
   color
   contact
   data
   document
   financial
   geo
   grammar
   identifier
   media
   medical
   numeric
   product
   publishing
   security
   software
   temporal
   text
   transport
   web

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Category
     - Validators
     - Guide
   * - :doc:`Address <address>`
     - 16
     - :doc:`../../library/address/index`
   * - :doc:`API <api>`
     - 12
     - :doc:`../../library/api/index`
   * - :doc:`Auth <auth>`
     - 19
     - :doc:`../../library/auth/index`
   * - :doc:`Color <color>`
     - 5
     - :doc:`../../library/color/index`
   * - :doc:`Contact <contact>`
     - 8
     - :doc:`../../library/contact/index`
   * - :doc:`Data <data>`
     - 14
     - :doc:`../../library/data/index`
   * - :doc:`Documents <document>`
     - 11
     - :doc:`../../library/document/index`
   * - :doc:`Finance <financial>`
     - 7
     - :doc:`../../library/financial/index`
   * - :doc:`Geo <geo>`
     - 8
     - :doc:`../../library/geo/index`
   * - :doc:`Grammar <grammar>`
     - 6
     - :doc:`../../library/grammar/index`
   * - :doc:`Identifiers <identifier>`
     - 26
     - :doc:`../../library/identifier/index`
   * - :doc:`Media <media>`
     - 11
     - :doc:`../../library/media/index`
   * - :doc:`Medical <medical>`
     - 4
     - :doc:`../../library/medical/index`
   * - :doc:`Numeric <numeric>`
     - 10
     - :doc:`../../library/numeric/index`
   * - :doc:`Product <product>`
     - 3
     - :doc:`../../library/product/index`
   * - :doc:`Publishing <publishing>`
     - 6
     - :doc:`../../library/publishing/index`
   * - :doc:`Security <security>`
     - 11
     - :doc:`../../library/security/index`
   * - :doc:`Software <software>`
     - 13
     - :doc:`../../library/software/index`
   * - :doc:`Temporal <temporal>`
     - 12
     - :doc:`../../library/temporal/index`
   * - :doc:`Text <text>`
     - 11
     - :doc:`../../library/text/index`
   * - :doc:`Transport <transport>`
     - 4
     - :doc:`../../library/transport/index`
   * - :doc:`Web <web>`
     - 11
     - :doc:`../../library/web/index`
