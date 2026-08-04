Aircraft
========

An `aircraft registration <https://en.wikipedia.org/wiki/Aircraft_registration>`__ is
the tail number painted on an airframe — ``N12345`` in the United States, ``G-ABCD``
in the United Kingdom. The country prefix is one or two letters, and most countries
separate it with a hyphen. **Aircraft** matches that shape.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(1, 2)``
:meth:`~edify.RegexBuilder.uppercase`, an :meth:`~edify.RegexBuilder.optional`
hyphen, then :meth:`~edify.RegexBuilder.between`\ ``(1, 5)`` uppercase alphanumerics.

National formats
----------------

.. edify-playground::

   from edify.library import aircraft

   aircraft("N12345")    # United States, no hyphen
   aircraft("G-ABCD")    # United Kingdom
   aircraft("D-AIBL")    # Germany
   aircraft("VH-OQA")    # Australia, a two-letter prefix
   aircraft("JA8089")    # Japan

Uppercase, prefix first
-----------------------

.. edify-playground::

   from edify.library import aircraft

   aircraft("G-ABCD")   # valid
   aircraft("g-abcd")   # lowercase
   aircraft("12345")    # no letter prefix
   aircraft("")         # empty

Each country has its own rules about what may follow the prefix, and this matches the
general shape rather than any one of them — so an invented registration passes. Check
the national registry to confirm an aircraft exists. For the service it operates see
:doc:`flight`.
