PMC
===

A `PubMed Central <https://www.ncbi.nlm.nih.gov/pmc/>`__ identifier names a full-text
article in the open-access repository. Unlike :doc:`pmid` it carries an explicit
``PMC`` prefix, which is what keeps the two apart.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``PMC`` then
:meth:`~edify.RegexBuilder.between`\ ``(1, 9)`` :meth:`~edify.RegexBuilder.digit`.

Identifiers
-----------

.. edify-playground::

   from edify.library import pmc

   pmc("PMC1234567")
   pmc("PMC1")
   pmc("PMC123456789")

The prefix is required
----------------------

.. edify-playground::

   from edify.library import pmc

   pmc("PMC1234567")   # prefixed
   pmc("1234567")      # bare digits: that shape is a PMID
   pmc("pmc1234567")   # the prefix is uppercase
   pmc("PMC")          # no number
   pmc("")             # empty

The same article usually has both a PMC identifier and a :doc:`pmid`, and the numbers
are unrelated — never derive one from the other. For the published version see
:doc:`doi`.
