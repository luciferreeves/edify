zip_code
========

:doc:`Library <../index>` › :doc:`Address <index>` › **zip_code**

``zip_code`` matches a US postal code — five digits, optionally followed by a
hyphen and four more (the ZIP+4 form).

.. code-block:: python

   from edify.library import zip_code

   zip_code("90210")        # True — five-digit ZIP
   zip_code("12345-6789")   # True — ZIP+4
   zip_code("1234")         # False — too few digits
   zip_code("abcde")        # False — digits only

What it matches
---------------

- **Five decimal digits**, optionally followed by ``-`` and **four more**.
- Anchored at both ends.

It does **not** check postal-service validity — every 5- and 5+4-digit string
matches, including unassigned or reserved ranges. Non-US postal codes belong to a
country-specific validator; see also the ``postal`` validator in the Geo category.

Try it
------

.. edify-playground::
   :tests: 90210|10001|12345-6789|1234|abcde

   from edify.library import zip_code
   zip_code

Pattern
-------

.. code-block:: text

   ^\d{5}(?:\-\d{4})?$
