Numeric
=======

Numbers in their written forms — integers, decimals, scientific notation,
percentages, fractions, ratios, and Roman numerals. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import integer, percentage, roman

   integer("-42")      # True
   percentage("99.9%") # True
   roman("MMXXIV")     # True

.. toctree::
   :hidden:

   fraction
   hash
   integer
   natural
   number
   ordinal
   percentage
   ratio
   roman
   scientific

Plain numbers
-------------

- :doc:`integer` — a signed whole number; :doc:`natural` — a positive one.
- :doc:`number` — any decimal, signed, with or without an exponent.
- :doc:`scientific` — a value that must carry an exponent.

Written forms
-------------

- :doc:`percentage` — a number with a ``%`` suffix.
- :doc:`fraction` — ``1/2`` and mixed numbers; :doc:`ratio` — ``16:9``.
- :doc:`ordinal` — ``1st``, ``2nd``; :doc:`roman` — ``MMXXIV``.

Digests
-------

- :doc:`hash` — a hexadecimal digest.
