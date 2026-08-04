Flight
======

A `flight number <https://en.wikipedia.org/wiki/Flight_number>`__ combines an
airline's two-character code with the route number — ``AA100``, ``BA2490`` — and
sometimes a trailing letter for a diverted or repositioned service. **Flight**
matches that shape.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(2)``
:meth:`~edify.RegexBuilder.uppercase`, then
:meth:`~edify.RegexBuilder.between`\ ``(1, 4)`` :meth:`~edify.RegexBuilder.digit`,
then an :meth:`~edify.RegexBuilder.optional` uppercase suffix.

Flight designators
------------------

.. edify-playground::

   from edify.library import flight

   flight("AA100")     # American Airlines 100
   flight("BA2490")    # British Airways
   flight("LH441")
   flight("UA1")       # a single-digit number
   flight("DL123A")    # with an operational suffix

Two letters, then digits
------------------------

.. edify-playground::

   from edify.library import flight

   flight("AA100")     # valid
   flight("aa100")     # lowercase
   flight("A100")      # a one-character airline code
   flight("AA")        # no number
   flight("AA12345")   # too many digits

Airline codes containing a digit — such as ``U2`` — match the two-character rule but
this pattern requires two *letters*, so they are rejected; use the ICAO
three-letter form if you need those. Flight numbers are also reused daily, so a
number identifies a service, not a specific flight — pair it with a date.
