PMID
====

A `PubMed identifier <https://pubmed.ncbi.nlm.nih.gov/>`__ names a citation in the
biomedical literature database. It is a plain sequential number, and **PMID** matches
1 to 8 digits.

The construction is :meth:`~edify.RegexBuilder.between`\ ``(1, 8)``
:meth:`~edify.RegexBuilder.digit`, anchored end to end. No prefix, no separators —
the bare number.

Identifiers
-----------

.. edify-playground::

   from edify.library import pmid

   pmid("12345678")   # a full-length identifier
   pmid("1")          # the earliest records have short numbers
   pmid("31978945")

Digits only
-----------

.. edify-playground::

   from edify.library import pmid

   pmid("12345678")     # valid
   pmid("PMID12345")    # the prefix is not part of the value
   pmid("123456789")    # too long
   pmid("")             # empty

The identifier is assigned sequentially, so the eight-digit ceiling reflects current
usage rather than a fixed rule — it will need widening eventually. Do not confuse a
PMID with a :doc:`pmc` identifier: they name different things and are not
interchangeable.
