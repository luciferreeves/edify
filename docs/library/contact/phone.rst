Phone
=====

**Phone** matches a telephone number as people write it — with or without a country
code, and with spaces, dots, hyphens, or parentheses as separators. It follows the
shape of `E.164 <https://www.itu.int/rec/T-REC-E.164/en>`__ numbers loosely rather
than enforcing one national format, because no single pattern fits every country.

The construction is an :func:`~edify.any_of` of two branches: an international form
— an optional ``+`` or ``00`` prefix, then groups of one to four digits joined by
optional separators — or a short bare run of digits for extensions and service
numbers.

International formats
---------------------

Country codes, grouping, and separator style all vary, and all are accepted:

.. edify-playground::

   from edify.library import phone

   phone("+1 555 123 4567")      # spaces
   phone("+44 20 7946 0958")     # a different country code
   phone("(555) 123-4567")       # parentheses and a hyphen
   phone("555.123.4567")         # dots
   phone("00 44 20 7946 0958")   # the 00 international prefix

Bare digit runs
---------------

A short unseparated number — an extension or a service code — also matches:

.. edify-playground::

   from edify.library import phone

   phone("5551234567")   # no separators
   phone("555")          # a short service number
   phone("12")           # the two-digit minimum

Not a phone number
------------------

Letters and empty input fail:

.. edify-playground::

   from edify.library import phone

   phone("+1 555 123 4567")   # valid
   phone("abc")               # letters
   phone("")                  # empty

This is deliberately permissive: it accepts many strings that are not dialable, and
it cannot tell you whether a number is assigned, reachable, or in the right country.
For real validation normalise to E.164 and check against a numbering-plan library —
or send a verification code. For the fax variant see :doc:`fax`; for pager codes,
:doc:`pager`.
