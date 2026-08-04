ORCID
=====

An `ORCID <https://orcid.org/>`__ identifies a researcher, so that their publications
stay attached to them across name changes, institutions, and the many people who
share a name. It is 16 digits in four hyphenated groups, with ``X`` permitted as the
final check character.

The construction is three groups of :meth:`~edify.RegexBuilder.exactly`\ ``(4)``
:meth:`~edify.RegexBuilder.digit` joined by hyphens, then three digits and an
:meth:`~edify.RegexBuilder.any_of` of a digit or ``X`` — the modulo-11 check
character needs a symbol for ten.

Researcher identifiers
----------------------

.. edify-playground::

   from edify.library import orcid

   orcid("0000-0002-1825-0097")
   orcid("0000-0001-5109-3700")
   orcid("0000-0002-1694-233X")   # an X check character

The grouping is fixed
---------------------

.. edify-playground::

   from edify.library import orcid

   orcid("0000-0002-1825-0097")   # hyphenated
   orcid("0000000218250097")      # bare digits
   orcid("0000-0002-1825-009")    # too short
   orcid("000X-0002-1825-0097")   # X only belongs at the end
   orcid("")                      # empty

The URL form ``https://orcid.org/0000-0002-1825-0097`` is not matched — strip the
prefix first. The final character is a computed checksum this cannot verify, so run
it before attributing work to an identifier.
