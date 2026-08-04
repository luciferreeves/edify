Publishing
==========

Every validator in the :doc:`publishing <../../library/publishing/index>` category. Each is a
callable :class:`~edify.Pattern`: pass a string to get a ``bool``, or compose it into a
larger pattern with :meth:`~edify.RegexBuilder.use`.

For what each one accepts and rejects, with runnable examples, see the
:doc:`library pages <../../library/publishing/index>`.

.. py:function:: edify.library.arxiv(value: str) -> bool

   arXiv. See :doc:`../../library/publishing/arxiv` for the full description.

   Emits ``^(?:\d{4}\.\d{4,5}(?:v\d+)?|[a-z]{2,10}(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)$``

.. py:function:: edify.library.doi(value: str) -> bool

   DOI. See :doc:`../../library/publishing/doi` for the full description.

   Emits ``^10\.\d{4,9}/[\-\._;\(\)/:A-Za-z0-9]+$``

.. py:function:: edify.library.isbn(value: str) -> bool

   ISBN. See :doc:`../../library/publishing/isbn` for the full description.

   Emits ``(?:^(?:\d[- ]?){9}(?:\d|[Xx])$|^(?:\d[- ]?){12}\d$)``

.. py:function:: edify.library.issn(value: str) -> bool

   ISSN. See :doc:`../../library/publishing/issn` for the full description.

   Emits ``^\d{4}\-\d{3}(?:\d|[Xx])$``

.. py:function:: edify.library.pmc(value: str) -> bool

   PMC. See :doc:`../../library/publishing/pmc` for the full description.

   Emits ``^PMC\d{1,9}$``

.. py:function:: edify.library.pmid(value: str) -> bool

   PMID. See :doc:`../../library/publishing/pmid` for the full description.

   Emits ``^\d{1,8}$``

