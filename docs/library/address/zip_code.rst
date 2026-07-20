zip_code
========

A US postal code comes in two shapes, and ``zip_code`` accepts both:

- **ZIP** — five digits, ``90210``. Leading zeros count: ``01001`` (Massachusetts)
  is real.
- **ZIP+4** — five digits, a hyphen, and four more, ``12345-6789``, narrowing
  delivery to a block or building.

.. edify-playground::
   :tests: 90210|01001|12345-6789|1234|123456|12345 6789

   from edify.library import zip_code
   zip_code

That is all it is — :meth:`~edify.RegexBuilder.exactly`\ ``(5)`` digits and an
:meth:`~edify.RegexBuilder.optional` ``-`` plus four more, emitting
``^\d{5}(?:\-\d{4})?$``. It checks the shape, not postal validity, and only US
codes; other countries live under the ``postal`` validator in the Geo category.
