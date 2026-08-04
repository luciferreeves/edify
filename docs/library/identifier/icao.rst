ICAO
====

An `ICAO code <https://www.icao.int/publications/DOC8643/Pages/Search.aspx>`__ is the
designator used in flight planning and air traffic control — three letters for an
airline, four for an airport. It is longer and more structured than the
:doc:`iata` code passengers see. **ICAO** matches both lengths.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(3, 4)``
:meth:`~edify.RegexBuilder.uppercase`, anchored end to end.

Airline and aerodrome codes
---------------------------

.. edify-playground::

   from edify.library import icao

   icao("AAL")    # American Airlines
   icao("BAW")    # British Airways
   icao("EGLL")   # London Heathrow
   icao("KJFK")   # New York Kennedy
   icao("RJAA")   # Tokyo Narita

Three or four uppercase letters
-------------------------------

.. edify-playground::

   from edify.library import icao

   icao("EGLL")    # four letters
   icao("egll")    # lowercase
   icao("EG")      # two: that is an IATA length
   icao("EGLLX")   # five
   icao("")        # empty

Unlike IATA codes, ICAO aerodrome codes are regionally structured — the first letter
or two identifies the region, so ``EG`` is the United Kingdom and ``K`` the
contiguous United States — but this pattern does not check that structure. For the
codes on your boarding pass see :doc:`iata`.
