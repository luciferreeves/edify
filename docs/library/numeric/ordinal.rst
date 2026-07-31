Ordinal
=======

**Ordinal** matches an English
`ordinal number <https://en.wikipedia.org/wiki/Ordinal_numeral>`__ — digits followed
by one of the four suffixes ``st``, ``nd``, ``rd``, ``th``.

The construction is :meth:`~edify.RegexBuilder.one_or_more`
:meth:`~edify.RegexBuilder.digit` followed by an :func:`~edify.any_of` over the four
suffixes, anchored end to end.

Ordinal forms
-------------

.. edify-playground::

   from edify.library import ordinal

   ordinal("1st")
   ordinal("2nd")
   ordinal("3rd")
   ordinal("4th")
   ordinal("21st")   # the suffix repeats for larger numbers
   ordinal("11th")   # the teens all take th

Digits and a known suffix
-------------------------

A spelled-out word or an invented suffix fails:

.. edify-playground::

   from edify.library import ordinal

   ordinal("5th")     # valid
   ordinal("first")   # spelled out
   ordinal("1")       # no suffix
   ordinal("1er")     # not an English suffix
   ordinal("")        # empty

The suffix is not checked against the number
--------------------------------------------

This is the caveat worth knowing: the pattern cannot tell that ``1`` takes ``st``,
so a mismatched pairing still matches:

.. edify-playground::

   from edify.library import ordinal

   ordinal("1st")   # correct
   ordinal("1th")   # wrong English, right shape
   ordinal("2th")   # likewise

Checking agreement needs arithmetic on the final digits — do that separately if it
matters. Only English suffixes are recognised. For the plain value see
:doc:`integer`.
