arXiv
=====

An `arXiv <https://arxiv.org/help/arxiv_identifier>`__ identifier names a preprint.
The scheme changed in 2007, so there are two forms: the modern ``YYMM.NNNNN`` and the
older ``subject-class/YYMMNNN``. **arXiv** accepts both, with an optional version
suffix.

The two forms are branches of an :func:`~edify.any_of`. Both allow a trailing ``vN``,
because a preprint can be revised and each revision is separately addressable.

Modern identifiers
------------------

.. edify-playground::

   from edify.library import arxiv

   arxiv("2401.12345")     # year 24, month 01
   arxiv("0704.0001")      # the first of the new scheme
   arxiv("2401.12345v2")   # the second version

Legacy identifiers
------------------

.. edify-playground::

   from edify.library import arxiv

   arxiv("math/0309136")        # a subject class
   arxiv("hep-th/9901001")      # a hyphenated class
   arxiv("math.GT/0309136")     # with a subdivision
   arxiv("cond-mat/0703470v1")  # with a version

Neither form is loose
---------------------

.. edify-playground::

   from edify.library import arxiv

   arxiv("2401.12345")   # valid
   arxiv("2401.123")     # too few digits
   arxiv("MATH/0309136") # subject classes are lowercase
   arxiv("")             # empty

An identifier without a version means "the latest", which is a moving target — cite
the versioned form when reproducibility matters. For the published article that a
preprint often becomes see :doc:`doi`.
