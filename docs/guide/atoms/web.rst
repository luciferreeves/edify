Web and file atoms
==================

Eight fragments for HTTP values, file naming, and colours — the pieces behind parts
of the :doc:`../../library/web/index` and :doc:`../../library/media/index`
categories.

Compose them into an anchored pattern rather than calling them directly; see
:doc:`index`.

HTTP values
-----------

``httpmethod`` is a closed set of the nine standard verbs — ``OPTIONS``, ``GET``,
``HEAD``, ``POST``, ``PUT``, ``DELETE``, ``TRACE``, ``CONNECT``, ``PATCH`` — and
uppercase only, matching the wire format.

``httpstatus`` is ``[1-5]\d{2}``: three digits with a leading digit in the 1–5
range, so it covers every defined class and rejects ``600`` and ``099``.

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
   status("599")       # the top of the 5xx class
   status("600")       # outside the 1xx-5xx range

Both are closed sets, so they will reject a value that is legitimate but new. That
is usually what you want at a boundary you control — and a reason to reach for
``unsigned`` instead if you are only logging.

Media types and file names
--------------------------

``mimetype`` is ``type/subtype``, both parts letter-led and allowing ``+``, ``-``,
and ``.`` after the first character. That covers structured suffixes like
``application/vnd.api+json``. A bare type with no subtype does not match.

``extension`` is a dot followed by alphanumerics — a **single** segment, so
``.tar.gz`` does not match as one extension.

``filename`` excludes the characters filesystems reject — ``/``, ``\``, ``<``,
``>``, ``:``, ``"``, ``|``, ``?``, ``*`` — and newlines. Note that it *does* allow
spaces, since real file names have them.

``filepath`` matches a whole path in either POSIX or Windows form.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import extension, filename, filepath, mimetype

   mt = Pattern().start_of_input().use(mimetype).end_of_input()
   ext = Pattern().start_of_input().use(extension).end_of_input()
   fn = Pattern().start_of_input().use(filename).end_of_input()
   fp = Pattern().start_of_input().use(filepath).end_of_input()

   mt("application/json")
   mt("application/vnd.api+json")   # structured suffixes work
   mt("text")                       # a subtype is required
   ext(".png")                      # the dot is part of it
   ext(".tar.gz")                   # one segment only
   ext("png")
   fn("report.pdf")
   fn("my file.txt")                # spaces are allowed in a name
   fn("a/b.txt")                    # separators are not part of a name
   fp("/usr/local/bin")
   fp("C:\\Windows")                # Windows paths too

Colours
-------

``hexcolor`` covers the 3-, 4-, 6-, and 8-digit forms, with the leading ``#``
required. Its branches are ordered longest-first — ``8|6|4|3`` — which is what
makes it match the full eight digits of ``#ff8800cc`` rather than stopping after
six. Branch order is invisible when the pattern is anchored and decisive when it
is not.

``rgbcolor`` matches the functional notation for both ``rgb()`` and ``rgba()``,
lowercase, with optional whitespace after each comma.

.. edify-playground::

   from edify import Pattern
   from edify.atoms import hexcolor, rgbcolor

   hexc = Pattern().start_of_input().use(hexcolor).end_of_input()
   rgb = Pattern().start_of_input().use(rgbcolor).end_of_input()

   hexc("#fff")
   hexc("#ff8800")
   hexc("#ff8800cc")     # with alpha
   hexc("ff8800")        # the hash is required
   hexc("#ff")           # and 3, 4, 6 or 8 digits exactly
   rgb("rgb(255, 136, 0)")
   rgb("rgba(255,136,0,1)")
   rgb("RGB(255,136,0)")   # lowercase only

Neither range-checks the numbers: ``rgb(999,999,999)`` matches the fragment. Use
:doc:`../../library/color/color` when the values matter.

Next: :doc:`finance`.
