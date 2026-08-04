Product
=======

Trade item numbers and manufacturer part identifiers. Each validator is a callable
:class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import gtin, barcode, mpn

   gtin("0012345600012")   # True
   barcode("012345678905") # True
   mpn("ABC-123")          # True

.. toctree::
   :hidden:

   barcode
   gtin
   mpn

Trade items
-----------

- :doc:`gtin` — a global trade item number at any of its four lengths.
- :doc:`barcode` — the alphanumeric payload of a scanned symbol.

Manufacturer references
-----------------------

- :doc:`mpn` — a manufacturer part number.
