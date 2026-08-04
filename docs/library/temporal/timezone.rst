Timezone
========

A `time zone <https://www.iana.org/time-zones>`__ is named rather than numeric —
``America/New_York``, ``Europe/London`` — because the offset it implies changes with
the season and with legislation. **Timezone** matches the IANA naming shape, plus the
UTC aliases and the short abbreviations.

The forms are the branches of an :func:`~edify.any_of`: a capitalised
``Area/Location`` path with one or more segments, the UTC designators (``UTC``,
``GMT``, ``UT``, ``Z``), or a 2–5 letter abbreviation.

IANA zone names
---------------

.. edify-playground::

   from edify.library import timezone

   timezone("America/New_York")
   timezone("Europe/London")
   timezone("Asia/Tokyo")
   timezone("America/Argentina/Buenos_Aires")   # a three-segment name
   timezone("Australia/Sydney")

UTC and abbreviations
---------------------

.. edify-playground::

   from edify.library import timezone

   timezone("UTC")
   timezone("GMT")
   timezone("Z")
   timezone("EST")    # an abbreviation
   timezone("AEST")

Capitalisation is required
--------------------------

IANA names capitalise each segment:

.. edify-playground::

   from edify.library import timezone

   timezone("America/New_York")   # correct
   timezone("america/new_york")   # lowercase
   timezone("America/")           # no location
   timezone("")                   # empty

Two caveats. Abbreviations are ambiguous — ``CST`` names at least three different
zones — so prefer full IANA names and treat abbreviations as display-only. And this
matches the *shape*, not the IANA database: an invented ``Country/City`` still passes,
so resolve the name with a zone library before relying on it. For a fixed
displacement see :doc:`offset`.
