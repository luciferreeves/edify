ISSN
====

An `ISSN <https://www.issn.org/>`__ identifies a serial publication — a journal,
magazine, or newspaper. It is eight characters written as two hyphenated groups of
four, with ``X`` permitted as the final check character. **ISSN** matches exactly
that.

The construction is :meth:`~edify.RegexBuilder.exactly`\ ``(4)``
:meth:`~edify.RegexBuilder.digit`, a ``-``, three more digits, then an
:meth:`~edify.RegexBuilder.any_of` of a digit or ``X`` — the modulo-11 check
character, in either case.

Serial identifiers
------------------

.. edify-playground::

   from edify.library import issn

   issn("0378-5955")
   issn("2049-3630")
   issn("0024-9319")
   issn("1050-124X")   # an X check character
   issn("1050-124x")   # lowercase x is accepted

The hyphen is required
----------------------

Unlike :doc:`isbn`, the grouping is fixed:

.. edify-playground::

   from edify.library import issn

   issn("0378-5955")   # hyphenated
   issn("03785955")    # bare digits
   issn("0378 5955")   # a space
   issn("0378-595")    # too short
   issn("")            # empty

The check character is positional here, not computed — ``0378-5956`` matches and is
not a real ISSN. Note also that print and electronic editions of the same title carry
different ISSNs, so an ISSN identifies a *medium* as well as a title. For books see
:doc:`isbn`.
