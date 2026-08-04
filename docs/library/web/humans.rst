humans.txt
==========

`humans.txt <https://humanstxt.org/>`__ is the counterpart to :doc:`robots` — a file
crediting the people who built a site rather than instructing the machines that
crawl it. Its convention is ``/* SECTION */`` markers followed by ``Field: value``
lines, and **humans.txt** matches those openings.

The branches of the :func:`~edify.any_of` are a ``/* … */`` section marker, a
``Field:`` line, or a ``#`` comment.

Sections and fields
-------------------

.. edify-playground::

   from edify.library import humans

   humans("/* TEAM */\nDeveloper: Jane Doe\nSite: example.com")
   humans("/* SITE */")
   humans("Developer: Jane Doe")
   humans("Last updated: 2024-01-01")
   humans("# a comment\nThanks: everyone")

A marker or field is required
-----------------------------

.. edify-playground::

   from edify.library import humans

   humans("Developer: Jane")   # a field line
   humans("hello world")       # prose with no field
   humans('{"a": 1}')          # JSON, not a section entry
   humans("")                  # empty

The format is a convention rather than a specification, so this is a light structural
check. Remember the file is public: crediting people by name is the point, but do not
put contact details there you would not publish elsewhere.
