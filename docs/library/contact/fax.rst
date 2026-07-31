Fax
===

A `fax <https://en.wikipedia.org/wiki/Fax>`__ number is a telephone number that
happens to reach a fax machine — there is no separate numbering plan, so **Fax**
matches the same shapes as :doc:`phone`, with its own slightly different grouping
rules.

The construction is an :meth:`~edify.RegexBuilder.optional` ``+`` and country code,
then groups of one to four :meth:`~edify.RegexBuilder.digit` characters joined by
optional space, hyphen, or dot separators, with an optional parenthesised area
code.

Written forms
-------------

.. edify-playground::

   from edify.library import fax

   fax("+1 555 123 4567")     # international with spaces
   fax("555-123-4567")        # national with hyphens
   fax("+44 20 7946 0958")    # another country
   fax("(555) 123-4567")      # a parenthesised area code

Not a number
------------

.. edify-playground::

   from edify.library import fax

   fax("555-123-4567")   # valid
   fax("abc")            # letters
   fax("")               # empty

Nothing distinguishes a fax number from a voice number by shape, so this cannot tell
you the far end is actually a fax machine. Use it for form validation and keep the
distinction in your data model. For the voice equivalent see :doc:`phone`.
