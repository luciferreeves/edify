ZIP Code
========

**ZIP Code** matches a US postal `ZIP code <https://en.wikipedia.org/wiki/ZIP_Code>`__
— the plain five-digit form or the extended ZIP+4. It is
:meth:`~edify.RegexBuilder.exactly`\ ``(5)`` digits and an
:meth:`~edify.RegexBuilder.optional` :meth:`~edify.RegexBuilder.group` of a ``-`` plus
four more digits, anchored end to end. Two details about the digits matter.

The five-digit ZIP
------------------

Exactly five decimal digits, and leading zeros are significant — real ZIPs like
``01001`` (Massachusetts) start with one, so **ZIP Code** never strips them:

.. edify-playground::

   from edify.library import zip_code

   zip_code("90210")    # a familiar one
   zip_code("01001")    # the leading zero is kept
   zip_code("1234")     # too few digits
   zip_code("123456")   # six digits is not a valid length
   zip_code("abcde")    # digits only

The ZIP+4 extension
-------------------

Optionally, a hyphen and four more digits, narrowing delivery to a block or building.
It is a **hyphen**, not a space:

.. edify-playground::

   from edify.library import zip_code

   zip_code("12345-6789")   # the extended form
   zip_code("90210-1234")   # another
   zip_code("12345 6789")   # a space, not a hyphen
   zip_code("12345-678")    # the extension needs four digits

It checks the shape, not postal-service validity, and only US codes — other countries
are handled by the **Postal** validator in the Geo category.
