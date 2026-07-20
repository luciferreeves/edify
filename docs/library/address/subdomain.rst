subdomain
=========

``subdomain`` matches a **single** DNS label — the ``api`` in ``api.example.com``
— not a dotted name.

Under the hood it is an :meth:`~edify.RegexBuilder.alphanumeric` first character,
:meth:`~edify.RegexBuilder.between`\ ``(0, 61)`` interior letters/digits/hyphens,
and an alphanumeric last character, anchored with
:meth:`~edify.RegexBuilder.start_of_input` / :meth:`~edify.RegexBuilder.end_of_input`.
Because it anchors on a first *and* a last alphanumeric, the minimum length is two:

.. code-block:: python

   from edify import Pattern

   subdomain = (
       Pattern().start_of_input()
       .alphanumeric()
       .between(0, 61).any_of().range("a", "z").range("A", "Z").range("0", "9").char("-").end()
       .alphanumeric()
       .end_of_input()
   )

which emits:

.. code-block:: text

   ^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$

A single label, 2 to 63 characters
----------------------------------

Letters, digits, and interior hyphens, with an alphanumeric first and last
character. A single character can't satisfy both ends, and 64 is one too many:

.. code-block:: python

   subdomain("api")        # True
   subdomain("my-sub")     # True — interior hyphen
   subdomain("staging-2")  # True — digits and hyphen
   subdomain("a1")         # True — the two-character minimum
   subdomain("a")          # False — too short for first + last
   subdomain("a" * 64)     # False — one over the 63-char maximum

.. edify-playground::
   :tests: api|my-sub|staging-2|a1|a

   from edify.library import subdomain
   subdomain

No hyphens at the ends, no dots
-------------------------------

A leading or trailing hyphen is rejected, and a dot makes it two labels rather
than one:

.. code-block:: python

   subdomain("-bad")   # False — can't start with a hyphen
   subdomain("bad-")   # False — can't end with a hyphen
   subdomain("a.b")    # False — a dot makes it two labels

.. edify-playground::
   :tests: staging|-bad|bad-|a.b

   from edify.library import subdomain
   subdomain

Notes
-----

- For a full dotted name use :doc:`domain` or :doc:`hostname`.
