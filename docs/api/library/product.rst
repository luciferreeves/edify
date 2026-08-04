Product
=======

Every validator in the :doc:`Product <../../library/product/index>` category.
Each is a callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or
compose it into a larger pattern with :meth:`~edify.RegexBuilder.use`.

Each entry states what the pattern guarantees, shows the chain that builds it, and
ends with the regex it emits. For prose, worked examples, and a live playground, use
the :doc:`library pages <../../library/product/index>`.

.. py:data:: edify.library.barcode

   Callable :class:`Pattern` for a generic barcode value shape.

   Full description: :doc:`Barcode <../../library/product/barcode>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      barcode = (
          Pattern()
          .start_of_input()
          .between(6, 48)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9]{6,48}$``

.. py:data:: edify.library.gtin

   Callable :class:`Pattern` for the GTIN family: 8-, 12-, 13-, or 14-digit barcode number.

   Full description: :doc:`GTIN <../../library/product/gtin>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern, any_of

      gtin = (
          Pattern()
          .start_of_input()
          .subexpression(
              any_of(
                  Pattern().exactly(8).digit(),
                  Pattern().exactly(12).digit(),
                  Pattern().exactly(13).digit(),
                  Pattern().exactly(14).digit(),
              )
          )
          .end_of_input()
      )

   **Emits** ``^(?:\d{8}|\d{12}|\d{13}|\d{14})$``

.. py:data:: edify.library.mpn

   Callable :class:`Pattern` for a permissive Manufacturer Part Number.

   Full description: :doc:`MPN <../../library/product/mpn>`

   **How it is built**

   .. code-block:: python

      from edify import Pattern

      mpn = (
          Pattern()
          .start_of_input()
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .end()
          .between(1, 63)
          .any_of()
          .range("A", "Z")
          .range("0", "9")
          .char("-")
          .char("_")
          .char(".")
          .end()
          .end_of_input()
      )

   **Emits** ``^[A-Z0-9][A-Z0-9\-_\.]{1,63}$``

