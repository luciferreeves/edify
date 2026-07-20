zip_code
========

``zip_code`` matches a US postal code. There are two accepted shapes — the
plain five-digit ZIP and the extended ZIP+4 — and a couple of details about digits
that catch people out.

.. edify-playground::
   :tests: 90210|01001|12345-6789|90210-1234|1234|123456|12345 6789|abcde

   from edify.library import zip_code
   zip_code

**The five-digit ZIP.** Exactly five decimal digits. Leading zeros are
significant — real ZIPs like ``01001`` (Massachusetts) start with one, so ``zip``
never strips them:

.. code-block:: python

   zip_code("90210")   # True
   zip_code("01001")   # True — the leading zero is kept
   zip_code("1234")    # False — too few digits
   zip_code("123456")  # False — six digits is not a valid ZIP length

**The ZIP+4 extension.** Optionally, a hyphen and four more digits, narrowing
delivery to a block or building. It is a **hyphen**, not a space:

.. code-block:: python

   zip_code("12345-6789")   # True
   zip_code("90210-1234")   # True
   zip_code("12345 6789")   # False — a space, not a hyphen
   zip_code("abcde")        # False — digits only

That is the whole thing: :meth:`~edify.RegexBuilder.exactly`\ ``(5)`` digits and an
:meth:`~edify.RegexBuilder.optional` ``-`` plus four more, emitting
``^\d{5}(?:\-\d{4})?$``. It checks the shape, not postal-service validity, and
only US codes — other countries live under the ``postal`` validator in the Geo
category.
