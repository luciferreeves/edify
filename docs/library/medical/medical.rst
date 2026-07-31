Medical code
============

**Medical code** matches the shapes used by the main clinical coding systems — an
`ICD-10 <https://icd.who.int/browse10/2019/en>`__ diagnosis code such as ``J45.909``,
a numeric identifier, or a hyphenated code.

The branches of the :func:`~edify.any_of` are: a 6–18 digit run, the ICD-10 pattern —
a letter (excluding ``U``), a digit, an alphanumeric, and an optional ``.`` plus up
to four characters — a ten-digit identifier, or digits with a single check digit
after a hyphen.

Diagnosis codes
---------------

.. edify-playground::

   from edify.library import medical

   medical("J45.909")   # asthma, unspecified
   medical("A01.1")     # a shorter subdivision
   medical("E11")       # a category with no subdivision
   medical("Z99.89")

Numeric identifiers
-------------------

.. edify-playground::

   from edify.library import medical

   medical("1234567890")     # a ten-digit identifier
   medical("123456")         # a six-digit code
   medical("123456-7")       # with a check digit

Not any string
--------------

.. edify-playground::

   from edify.library import medical

   medical("J45.909")   # a valid shape
   medical("abc")       # letters alone
   medical("")          # empty

Accepting several systems at once means a match does not tell you *which* system a
code belongs to, and shape says nothing about whether a code is current — coding
systems are revised, and retired codes keep their shape. Validate against the
official code set before using a value clinically or for billing.
