zip_code
========

:doc:`Library <../index>` › :doc:`Address <index>` › **zip_code**

``zip_code`` matches a US postal code in either of its two shapes: the five-digit
ZIP and the nine-digit ZIP+4.

.. code-block:: python

   from edify.library import zip_code

   zip_code("90210")   # True

The five-digit ZIP
------------------

Exactly five decimal digits — leading zeros included, since real ZIPs like
``01001`` (Massachusetts) begin with one:

.. code-block:: python

   zip_code("90210")   # True
   zip_code("10001")   # True
   zip_code("01001")   # True — leading zero preserved

The ZIP+4 extension
-------------------

Optionally, a hyphen and four more digits — the ZIP+4 form that narrows delivery
to a block or building:

.. code-block:: python

   zip_code("12345-6789")   # True
   zip_code("90210-1234")   # True

What it rejects
---------------

.. code-block:: python

   zip_code("1234")         # False — too few digits
   zip_code("123456")       # False — six digits (not a valid ZIP length)
   zip_code("12345 6789")   # False — the +4 uses a hyphen, not a space
   zip_code("abcde")        # False — digits only

``zip_code`` checks the *shape* — every 5- and 5+4-digit string matches, including
unassigned ranges. It does not cover non-US postal codes; for those see the
``postal`` validator in the Geo category.

Pattern
-------

.. code-block:: text

   ^\d{5}(?:\-\d{4})?$
