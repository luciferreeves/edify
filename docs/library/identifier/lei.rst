LEI
===

A `Legal Entity Identifier <https://www.gleif.org/en/about-lei/introducing-the-legal-entity-identifier-lei>`__
identifies a party to a financial transaction — the entity, not the security. It is
20 characters: a four-character issuer prefix, two reserved zeros, twelve entity
characters, and two check digits. **LEI** matches that length and alphabet.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(20)`` over an
:meth:`~edify.RegexBuilder.any_of` class of uppercase letters and digits.

Entity identifiers
------------------

.. edify-playground::

   from edify.library import lei

   lei("529900T8BM49AURSDO55")
   lei("5493001KJTIIGC8Y1R12")
   lei("213800QILIUD4ROSUO03")

Twenty uppercase alphanumerics
------------------------------

.. edify-playground::

   from edify.library import lei

   lei("529900T8BM49AURSDO55")    # twenty characters
   lei("529900t8bm49aursdo55")    # lowercase
   lei("529900T8BM49AURSDO5")     # nineteen
   lei("529900T8BM49AURSDO555")   # twenty-one
   lei("")                        # empty

The final two characters are a mod-97 checksum that this cannot compute, and the
internal structure — the reserved zeros at positions 5 and 6 — is not enforced.
Verify an LEI against the GLEIF register, which will also tell you whether the
registration is current: an LEI must be renewed annually, and a lapsed one is still
well formed.
