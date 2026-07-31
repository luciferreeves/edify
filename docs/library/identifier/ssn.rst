SSN
===

A `US social security number <https://www.ssa.gov/employer/randomization.html>`__ is
three groups of digits — ``123-45-6789``. **SSN** does more than count digits: it
excludes the ranges the Social Security Administration never issues, which catches
both typos and the obviously fake numbers used in test data.

The exclusions are written with :meth:`~edify.RegexBuilder.assert_not_ahead`: the
area number may not be ``000``, ``666``, or anything from ``900`` up; the group
number may not be ``00``; the serial may not be ``0000``.

Valid numbers
-------------

.. edify-playground::

   from edify.library import ssn

   ssn("123-45-6789")
   ssn("001-01-0001")   # the lowest issuable number
   ssn("899-99-9999")

Never-issued ranges
-------------------

These are the checks that make the validator worth using:

.. edify-playground::

   from edify.library import ssn

   ssn("123-45-6789")   # issuable
   ssn("000-45-6789")   # area 000 is never issued
   ssn("666-45-6789")   # area 666 is never issued
   ssn("900-45-6789")   # 900 and above are reserved
   ssn("123-00-6789")   # group 00 is never issued
   ssn("123-45-0000")   # serial 0000 is never issued

Hyphens are required
--------------------

.. edify-playground::

   from edify.library import ssn

   ssn("123-45-6789")   # hyphenated
   ssn("123456789")     # bare digits
   ssn("")              # empty

An SSN is highly sensitive personal data. Validate it only where you genuinely need
it, never log it, and note that matching says nothing about whether a number was
issued to the person presenting it. For the taxpayer variant see :doc:`itin`; for
either form, :doc:`tin`.
