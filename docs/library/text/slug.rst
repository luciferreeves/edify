Slug
====

A `slug <https://developer.mozilla.org/en-US/docs/Glossary/Slug>`__ is the
human-readable part of a URL — lowercase words joined by single hyphens, with no
leading, trailing, or doubled separators. **Slug** enforces exactly that.

The construction is :meth:`~edify.RegexBuilder.one_or_more` of a lowercase
alphanumeric run, followed by :meth:`~edify.RegexBuilder.zero_or_more` groups of
"hyphen plus another run". Because each hyphen must be followed by a run, the
doubled and dangling cases are impossible by construction rather than excluded by a
separate rule.

Well-formed slugs
-----------------

.. edify-playground::

   from edify.library import slug

   slug("hello-world")            # the canonical form
   slug("post")                   # a single segment
   slug("2024-year-in-review")    # digits are fine
   slug("a-b-c-d-e")              # any number of segments

Hyphens must separate
---------------------

A hyphen only ever appears between two runs:

.. edify-playground::

   from edify.library import slug

   slug("hello-world")    # separated
   slug("-hello")         # leading hyphen
   slug("hello-")         # trailing hyphen
   slug("hello--world")   # doubled hyphen

Lowercase only
--------------

Slugs are case-normalised so that one URL maps to one resource — uppercase,
underscores, and spaces must be transformed before validating:

.. edify-playground::

   from edify.library import slug

   slug("hello-world")   # normalised
   slug("Hello-World")   # uppercase
   slug("hello_world")   # underscore: see word
   slug("hello world")   # a space

This validates the shape of an already-normalised slug; it does not transliterate
accents or strip punctuation for you. For the underscore-bearing identifier form see
:doc:`word`, and for the URL path a slug sits in, :doc:`../address/url`.
