Favicon
=======

A `favicon <https://en.wikipedia.org/wiki/Favicon>`__ is the small icon a browser
shows beside a page title. **Favicon** matches a path ending in ``favicon`` with one
of the four formats browsers accept: ``.ico``, ``.png``, ``.svg``, or ``.gif``.

The construction is :meth:`~edify.RegexBuilder.zero_or_more` directory segments —
each a run excluding separators and control codes — then the literal ``favicon.``
and an :func:`~edify.any_of` over the four extensions.

Icon paths
----------

.. edify-playground::

   from edify.library import favicon

   favicon("favicon.ico")            # the classic root icon
   favicon("favicon.png")
   favicon("favicon.svg")
   favicon("static/favicon.ico")     # in a subdirectory
   favicon("assets/img/favicon.png")

The name and format are fixed
-----------------------------

.. edify-playground::

   from edify.library import favicon

   favicon("favicon.ico")   # valid
   favicon("icon.png")      # a different name
   favicon("favicon.jpg")   # not a supported format
   favicon("/favicon.ico")  # a leading slash makes an empty first segment

Note the leading-slash case: an absolute path does not match, because the pattern
expects each segment to be non-empty. Strip the leading ``/`` first. For a general
file name see :doc:`filename`.
