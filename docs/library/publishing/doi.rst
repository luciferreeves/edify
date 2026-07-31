DOI
===

A `DOI <https://www.doi.org/>`__ is a permanent identifier for a document — an
article, a dataset, a report. It always begins ``10.``, followed by a registrant
prefix and a suffix the registrant chooses. **DOI** matches that structure.

The construction is the :meth:`~edify.RegexBuilder.string` literal ``10.``, then
:meth:`~edify.RegexBuilder.between`\ ``(4, 9)`` :meth:`~edify.RegexBuilder.digit` for
the registrant, a ``/``, and a suffix over a broad character class — because
registrants are free to choose almost any suffix.

Identifiers
-----------

.. edify-playground::

   from edify.library import doi

   doi("10.1000/xyz123")
   doi("10.1038/nature12373")
   doi("10.1109/5.771073")            # dots in the suffix
   doi("10.1007/978-3-030-12345-6_7") # hyphens and underscores
   doi("10.5555/(test);sub:1")        # the suffix set is deliberately wide

The ``10.`` prefix is required
------------------------------

.. edify-playground::

   from edify.library import doi

   doi("10.1000/xyz123")   # valid
   doi("11.1000/xyz123")   # DOIs always start 10.
   doi("10.1000")          # no suffix
   doi("10.100/x")         # registrant too short
   doi("")                 # empty

A URL-form DOI — ``https://doi.org/10.1000/xyz123`` — is not matched; strip the
resolver prefix first. Matching also does not mean the DOI resolves: only the
registry can tell you that, and a well-formed identifier may point at nothing. For
preprints see :doc:`arxiv`.
