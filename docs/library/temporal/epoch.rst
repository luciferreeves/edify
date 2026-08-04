Epoch
=====

`Unix time <https://en.wikipedia.org/wiki/Unix_time>`__ counts seconds since
1 January 1970. **Epoch** matches that count: up to ten digits, with an optional
leading ``-`` for times before the epoch.

The construction is an :meth:`~edify.RegexBuilder.optional` ``-`` then
:meth:`~edify.RegexBuilder.between`\ ``(1, 10)`` :meth:`~edify.RegexBuilder.digit`,
anchored end to end. The ten-digit ceiling is what keeps this to *seconds* —
millisecond values are longer, and belong to :doc:`timestamp`.

Second counts
-------------

.. edify-playground::

   from edify.library import epoch

   epoch("1700000000")   # a recent timestamp
   epoch("0")            # the epoch itself
   epoch("-86400")       # a day before the epoch
   epoch("1")            # a single digit

Seconds, not milliseconds
-------------------------

A thirteen-digit value is milliseconds, and mixing the two units is a common and
costly bug:

.. edify-playground::

   from edify.library import epoch

   epoch("1700000000")      # ten digits: seconds
   epoch("1700000000000")   # thirteen digits: milliseconds
   epoch("1.7e9")           # scientific notation
   epoch("abc")             # not digits
   epoch("")                # empty

The digit ceiling is a length check, not a range check, so ``9999999999`` matches
even though it lands in the year 2286. If a value must fall in a plausible window,
compare it after parsing. For a validator that accepts both units see
:doc:`timestamp`.
