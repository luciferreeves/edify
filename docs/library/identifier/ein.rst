EIN
===

An `EIN <https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers>`__
identifies a business for US tax purposes — the corporate counterpart to an
:doc:`ssn`. It is two digits, a hyphen, then seven more. **EIN** matches exactly
that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(2)``
:meth:`~edify.RegexBuilder.digit`, a ``-``, then
:meth:`~edify.RegexBuilder.exactly`\ ``(7)`` digits.

Employer numbers
----------------

.. edify-playground::

   from edify.library import ein

   ein("12-3456789")
   ein("00-0000000")   # shape-valid
   ein("99-9999999")

The grouping is fixed
---------------------

The 2–7 split is what distinguishes an EIN from the 3–2–4 of an :doc:`ssn`:

.. edify-playground::

   from edify.library import ein

   ein("12-3456789")    # correct grouping
   ein("123456789")     # no hyphen
   ein("123-45-6789")   # that is an SSN
   ein("12-345678")     # too few digits
   ein("")              # empty

The first two digits are a prefix that used to encode the issuing office, but this
does not check them against the assigned list, and an EIN has no check digit —
verify with the IRS if the number matters. For either US taxpayer form see
:doc:`tin`.
