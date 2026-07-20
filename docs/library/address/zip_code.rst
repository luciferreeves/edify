zip_code
========

``zip_code`` matches a US postal code in either of its two shapes — the
five-digit ZIP and the nine-digit ZIP+4.

Under the hood it is :meth:`~edify.RegexBuilder.exactly`\ ``(5)`` of a
:meth:`~edify.RegexBuilder.digit`, then an :meth:`~edify.RegexBuilder.optional`
group of ``-`` plus four more digits, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`:

.. code-block:: python

   from edify import Pattern

   zip_code = (
       Pattern().start_of_input()
       .exactly(5).digit()
       .optional().group().char("-").exactly(4).digit().end()
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^\d{5}(?:\-\d{4})?$

The five-digit ZIP
------------------

Exactly five decimal digits, leading zeros included — real ZIPs like ``01001``
(Massachusetts) begin with one. Too few or too many digits fail:

.. code-block:: python

   zip_code("90210")   # True
   zip_code("10001")   # True
   zip_code("01001")   # True — leading zero preserved
   zip_code("1234")    # False — too few digits
   zip_code("123456")  # False — six digits is not a valid ZIP length

.. edify-playground::
   :tests: 90210|10001|01001|1234|123456

   from edify.library import zip_code
   zip_code

The ZIP+4 extension
-------------------

Optionally, a hyphen and four more digits — the ZIP+4 form that narrows delivery
to a block or building. It uses a hyphen, not a space:

.. code-block:: python

   zip_code("12345-6789")   # True
   zip_code("90210-1234")   # True
   zip_code("12345 6789")   # False — the +4 uses a hyphen, not a space

.. edify-playground::
   :tests: 12345-6789|90210-1234|12345 6789|abcde

   from edify.library import zip_code
   zip_code

Notes
-----

- ``zip_code`` checks the *shape* — every 5- and 5+4-digit string matches,
  including unassigned ranges. It does not cover non-US postal codes; for those
  see the ``postal`` validator in the Geo category.
