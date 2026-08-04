SKU
===

A `stock keeping unit <https://en.wikipedia.org/wiki/Stock_keeping_unit>`__ is a
retailer's own code for an item — internal, unstandardised, and free-form. **SKU**
matches the permissive shape such codes take: 4 to 20 characters of letters, digits,
and the separators ``-``, ``_``, ``.``, and ``/``.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(4, 20)`` over an
:meth:`~edify.RegexBuilder.any_of` class. Case is not constrained, because retailers
differ.

Stock codes
-----------

.. edify-playground::

   from edify.library import sku

   sku("ABC-1234")
   sku("shirt_blue_L")
   sku("PROD.2024.001")
   sku("cat/sub/item1")
   sku("A1B2")            # the four-character minimum

Within range
------------

.. edify-playground::

   from edify.library import sku

   sku("ABC-1234")               # valid
   sku("ABC")                    # too short
   sku("A" * 21)                 # too long
   sku("ABC 1234")               # spaces are not permitted
   sku("")                       # empty

Because SKUs are internal, a match means only "plausibly formatted" — the same code
means different things at different retailers, and nothing here can check yours. Use
:doc:`../product/gtin` when you need a globally meaningful item number.
