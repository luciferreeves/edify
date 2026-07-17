:orphan:

Edify
=====

Build regex you can actually read.

Edify is a fluent, immutable regex builder for Python. Describe the pattern in
plain English, get a compiled regular expression your teammates can actually
review.

.. code-block:: python

   from edify import Pattern

   four_digits = Pattern().start_of_input().exactly(4).digit().end_of_input()
   four_digits.to_regex_string()   # -> '^\\d{4}$'

This site is being rebuilt. The full guide, library reference, and interactive
playground are on their way.
