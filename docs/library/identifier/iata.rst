IATA
====

An `IATA code <https://www.iata.org/en/publications/directories/code-search/>`__ is
the short designator used on tickets and baggage tags — two letters for an airline,
three for an airport. **IATA** matches both lengths.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(2, 3)``
:meth:`~edify.RegexBuilder.uppercase`, anchored end to end.

Airline and airport codes
-------------------------

.. edify-playground::

   from edify.library import iata

   iata("AA")    # American Airlines
   iata("BA")    # British Airways
   iata("LHR")   # London Heathrow
   iata("JFK")   # New York Kennedy
   iata("NRT")   # Tokyo Narita

Two or three uppercase letters
------------------------------

.. edify-playground::

   from edify.library import iata

   iata("LHR")    # three letters
   iata("lhr")    # lowercase
   iata("L")      # one letter
   iata("LHRX")   # four: that is an ICAO length
   iata("U2")     # airline codes containing digits are not matched
   iata("")       # empty

Two limitations worth knowing. Airline codes that contain a digit — ``U2``, ``4X`` —
are rejected because the pattern requires letters. And IATA codes are reassigned when
an airline or airport closes, so a code is not a permanent identifier. For the
four-letter equivalents see :doc:`icao`.
