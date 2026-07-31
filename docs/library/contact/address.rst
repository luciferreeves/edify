Address
=======

**Address** matches a street address in the shape used across
`much of the world <https://en.wikipedia.org/wiki/Address>`__: a building number
first, then whitespace, then the street name and any unit information.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit`, then :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.whitespace_char`, then a run of letters, digits, spaces,
and the punctuation addresses carry — ``.`` ``,`` ``'`` ``-`` ``#`` ``/``.

Street addresses
----------------

.. edify-playground::

   from edify.library import address

   address("123 Main St")
   address("1600 Pennsylvania Ave NW")
   address("42 O'Connell Street")        # an apostrophe
   address("10 Downing St, Apt #3")      # a unit number
   address("5 Rue de l'Église")          # accented letters are not in the class

The number comes first
----------------------

This is the rule that shapes everything: an address with no leading number, or one
where the name precedes the number, does not match:

.. edify-playground::

   from edify.library import address

   address("123 Main St")        # number first
   address("Main St")            # no number
   address("221B Baker Street")  # the number must be digits alone
   address("")                   # empty

Address formats vary enormously — house names instead of numbers, numbers written
after the street, and non-Latin scripts are all normal somewhere, and none of them
match here. Treat this as a light check for a single-line form field, never as a
test of whether an address exists; only an address-verification service can tell you
that. For the postal code that accompanies it see :doc:`../address/zip_code`.
