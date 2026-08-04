Publishing
==========

Identifiers for books, journals, articles, and preprints. Each validator is a
callable :class:`~edify.Pattern`: import it, call it with a string, get a ``bool``.

.. code-block:: python

   from edify.library import isbn, doi, arxiv

   isbn("978-3-16-148410-0")   # True
   doi("10.1038/nature12373")  # True
   arxiv("2401.12345")         # True

.. toctree::
   :hidden:

   arxiv
   doi
   isbn
   issn
   pmc
   pmid

Books and journals
------------------

- :doc:`isbn` — a book identifier; :doc:`issn` — a serial identifier.

Articles and preprints
----------------------

- :doc:`doi` — a digital object identifier.
- :doc:`arxiv` — a preprint identifier.
- :doc:`pmid` and :doc:`pmc` — the two biomedical literature identifiers.
