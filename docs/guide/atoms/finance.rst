Finance and version atoms
=========================

Four fragments: three financial identifiers and the semantic version number. They
are the pieces behind :doc:`../../library/financial/card`,
:doc:`../../library/identifier/iban`, and
:doc:`../../library/software/semver`.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

Payment and banking
-------------------

``creditcard`` is a bare 13–19 digit run, ``iban`` a country code with check digits
and an account part, ``bic`` a bank identifier.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import creditcard, iban, bic

   card = Pattern().start_of_input().use(creditcard).end_of_input()
   account = Pattern().start_of_input().use(iban).end_of_input()
   bank = Pattern().start_of_input().use(bic).end_of_input()

   card("4111111111111111")            # digits only, no separators
   card("4111 1111 1111 1111")         # the atom has no separator handling
   account("GB82WEST12345698765432")
   bank("DEUTDEFF")                    # eight characters
   bank("DEUTDEFF500")                 # or eleven

Note that ``creditcard`` accepts only unseparated digits — the spaces and hyphens
people actually type are handled by the :doc:`../../library/financial/card`
validator, not the atom. And as everywhere in this library, the check digits these
identifiers carry are **not** verified by the pattern; run the checksum yourself.

Versions
--------

``semver`` is the three-component core of a semantic version, without the
pre-release and build metadata the full :doc:`../../library/software/semver`
validator accepts.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import semver

   version = Pattern().start_of_input().use(semver).end_of_input()

   version("1.2.3")
   version("0.1.0")
   version("01.2.3")        # leading zeros are not allowed
   version("1.2")           # all three components are required
   version("1.2.3-alpha")   # suffixes need the library validator

Next: :doc:`grouping`.
