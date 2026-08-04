ITIN
====

An `ITIN <https://www.irs.gov/individuals/individual-taxpayer-identification-number>`__
is issued to people who must file US taxes but cannot get an :doc:`ssn`. It takes the
same three-group shape but always begins with ``9``, and its middle group falls in
specific assigned ranges. **ITIN** enforces both.

The area is ``9`` followed by two digits; the group is an :func:`~edify.any_of` over
the assigned ranges — ``50``–``65``, ``70``–``88``, ``90``–``92``, ``94``–``99`` —
which is what distinguishes an ITIN from a malformed SSN.

Valid numbers
-------------

.. edify-playground::

   from edify.library import itin

   itin("912-70-1234")
   itin("999-88-9999")
   itin("900-50-0000")
   itin("955-94-1234")

The group ranges are enforced
-----------------------------

.. edify-playground::

   from edify.library import itin

   itin("912-70-1234")   # group 70 is assigned
   itin("912-49-1234")   # 49 is below the assigned ranges
   itin("912-66-1234")   # 66 falls in a gap
   itin("912-93-1234")   # 93 falls in a gap

It must start with 9
--------------------

.. edify-playground::

   from edify.library import itin

   itin("912-70-1234")   # starts with 9
   itin("123-70-1234")   # that is an SSN shape
   itin("912701234")     # hyphens are required
   itin("")              # empty

Like an :doc:`ssn`, an ITIN is sensitive tax data — collect it only when required.
Matching the assigned ranges does not mean the number was issued. For either form see
:doc:`tin`.
