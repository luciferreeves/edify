Altitude
========

**Altitude** matches a `height <https://en.wikipedia.org/wiki/Altitude>`__ value with
an optional unit — ``100m``, ``1000 ft``, ``-50m``. Negative values are accepted,
since positions below sea level are real.

The construction is an :meth:`~edify.RegexBuilder.optional` ``-``, digits, an optional
fractional part, optional whitespace, and an :meth:`~edify.RegexBuilder.optional`
unit from ``m``, ``ft``, ``km``, or ``mi``.

Values and units
----------------

.. edify-playground::

   from edify.library import altitude

   altitude("100m")       # metres
   altitude("1000 ft")    # feet, with a space
   altitude("8.848km")    # a fractional value
   altitude("-50m")       # below sea level
   altitude("500")        # the unit is optional

Known units only
----------------

.. edify-playground::

   from edify.library import altitude

   altitude("100m")     # a known unit
   altitude("100yd")    # yards are not in the set
   altitude("abc")      # not a number
   altitude("")         # empty

Because the unit is optional, a bare number is ambiguous — and confusing feet with
metres is a documented cause of aviation and engineering incidents. Store the unit
explicitly rather than relying on convention. No range is enforced either, so
implausible altitudes match.
