Web and file atoms
==================

Eight fragments for HTTP values, file naming, and colours — the pieces behind parts
of the :doc:`../../library/web/index` and :doc:`../../library/media/index`
categories.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

HTTP values
-----------

``httpmethod`` is a closed set of verbs; ``httpstatus`` is any three-digit code in
the 1xx–5xx range.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import httpmethod, httpstatus

   method = Pattern().start_of_input().use(httpmethod).end_of_input()
   status = Pattern().start_of_input().use(httpstatus).end_of_input()

   method("GET")
   method("PATCH")
   method("BREW")      # not a standard method
   method("get")       # methods are uppercase
   status("404")
   status("600")       # outside the 1xx-5xx range

Media types and file names
--------------------------

``mimetype`` is ``type/subtype``; ``extension`` includes the leading dot;
``filename`` excludes path separators and the characters filesystems reject;
``filepath`` matches a whole path.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import mimetype, extension, filename, filepath

   mt = Pattern().start_of_input().use(mimetype).end_of_input()
   ext = Pattern().start_of_input().use(extension).end_of_input()
   fn = Pattern().start_of_input().use(filename).end_of_input()
   fp = Pattern().start_of_input().use(filepath).end_of_input()

   mt("application/json")
   mt("text")            # a subtype is required
   ext(".png")           # the dot is part of it
   ext("png")
   fn("report.pdf")
   fn("a/b.txt")         # separators are not part of a name
   fp("/usr/local/bin")

Colours
-------

``hexcolor`` covers the 3-, 4-, 6-, and 8-digit forms; ``rgbcolor`` matches the
functional notation.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hexcolor, rgbcolor

   hexc = Pattern().start_of_input().use(hexcolor).end_of_input()
   rgb = Pattern().start_of_input().use(rgbcolor).end_of_input()

   hexc("#fff")
   hexc("#ff8800")
   hexc("#ff8800cc")     # with alpha
   hexc("ff8800")        # the hash is required
   rgb("rgb(255,136,0)")
   rgb("rgba(255,136,0)")

Next: :doc:`finance`.
