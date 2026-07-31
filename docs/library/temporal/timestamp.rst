Timestamp
=========

**Timestamp** matches a numeric `Unix timestamp <https://en.wikipedia.org/wiki/Unix_time>`__
in either of the units systems actually emit: seconds (ten digits) or milliseconds
(thirteen). It is the validator for a field whose unit you do not control.

The construction is an :meth:`~edify.RegexBuilder.optional` ``-`` then
:meth:`~edify.RegexBuilder.between`\ ``(10, 13)`` :meth:`~edify.RegexBuilder.digit`.
The wider band is the difference from :doc:`epoch`, which caps at ten.

Seconds and milliseconds
------------------------

.. edify-playground::

   from edify.library import timestamp

   timestamp("1700000000")      # ten digits: seconds
   timestamp("1700000000000")   # thirteen digits: milliseconds
   timestamp("1700000000123")   # milliseconds with precision
   timestamp("-1000000000")     # before the epoch

Numeric only
------------

An ISO datetime is a timestamp in the general sense but not a numeric one:

.. edify-playground::

   from edify.library import timestamp

   timestamp("1700000000")             # numeric
   timestamp("2024-01-15T10:30:00Z")   # ISO form: see datetime
   timestamp("170000")                 # too few digits
   timestamp("17000000000000")         # too many
   timestamp("")                       # empty

Because both units match, the digit count is the *only* way to tell them apart —
check the length before converting, or you will be off by a factor of a thousand. For
seconds alone see :doc:`epoch`; for the textual form, :doc:`datetime`.
