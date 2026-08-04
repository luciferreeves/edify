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

``creditcard`` is ``\d{13,19}`` — a bare run of digits in the length range card
numbers occupy. It has no separator handling at all, so the spaces and hyphens
people actually type must be stripped first, or matched by
:doc:`../../library/financial/card`.

``iban`` is a two-letter country code, two check digits, and 11–30 alphanumerics.
``bic`` is four letters for the bank, two for the country, two alphanumerics for
the location, and an optional three-character branch — so it is either eight or
eleven characters, never nine or ten.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import bic, creditcard, iban

   card = Pattern().start_of_input().use(creditcard).end_of_input()
   account = Pattern().start_of_input().use(iban).end_of_input()
   bank = Pattern().start_of_input().use(bic).end_of_input()

   card("4111111111111111")            # digits only, no separators
   card("4111 1111 1111 1111")         # the atom has no separator handling
   card("411111111111")                # twelve digits is too short
   account("GB82WEST12345698765432")
   account("gb82west12345698765432")   # uppercase only
   bank("DEUTDEFF")                    # eight characters
   bank("DEUTDEFF500")                 # or eleven
   bank("DEUTDEFF5")                   # never nine

All three carry check digits that the pattern does **not** verify. A ``creditcard``
match tells you the digits are the right length, not that the Luhn checksum passes;
an ``iban`` match tells you the shape is right, not that the mod-97 check does. Run
the checksum yourself after the pattern accepts — that is arithmetic, and no
regular expression can do it.

Versions
--------

``semver`` is the three-component core of a semantic version: three numbers joined
by dots, each either ``0`` or a non-zero-led run of digits. That last rule is what
rejects ``01.2.3`` — leading zeros are not valid in a semantic version, and the
alternation ``(?:[1-9]\d*|[0])`` encodes the rule rather than approximating it with
``\d+``.

What it does *not* cover is the pre-release and build metadata — the ``-alpha.1``
and ``+build.5`` suffixes. Those need the full
:doc:`../../library/software/semver` validator.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import semver

   version = Pattern().start_of_input().use(semver).end_of_input()

   version("1.2.3")
   version("0.1.0")         # zero components are fine
   version("01.2.3")        # leading zeros are not allowed
   version("1.2")           # all three components are required
   version("1.2.3-alpha")   # suffixes need the library validator

Because it is unanchored, ``semver`` composes cleanly into a larger pattern — a
tag name, a filename, a changelog heading — where the version sits beside other
text:

.. code-block:: python

   from edify import Pattern
   from edify.atoms import semver

   tag = Pattern().start_of_input().char("v").use(semver).end_of_input()
   tag.to_regex_string()
   # '^v(?:[1-9]\\d*|[0])\\.(?:[1-9]\\d*|[0])\\.(?:[1-9]\\d*|[0])$'

Next: :doc:`grouping`.
