Encoding
========

An HTTP `content coding <https://datatracker.ietf.org/doc/html/rfc9110#field.content-encoding>`__
names the compression applied to a response body — ``gzip``, ``br``, ``zstd``.
Unlike :doc:`charset`, which is an open registry of names, the codings in everyday
use are a short closed list, so **Encoding** matches that list exactly.

The construction is an :func:`~edify.any_of` over the registered tokens, plus ``*``
for the wildcard used in ``Accept-Encoding``, followed by an
:meth:`~edify.RegexBuilder.optional` ``;q=`` quality value.

Content codings
---------------

.. edify-playground::

   from edify.library import encoding

   encoding("gzip")
   encoding("br")           # Brotli
   encoding("zstd")
   encoding("deflate")
   encoding("identity")     # no transformation
   encoding("*")            # the Accept-Encoding wildcard

Quality values
--------------

``Accept-Encoding`` attaches a preference weight to each coding:

.. edify-playground::

   from edify.library import encoding

   encoding("gzip;q=0.8")
   encoding("br;q=1.0")
   encoding("gzip;q=1")

A closed set of names
---------------------

An unregistered coding, or a character-set name, is not a content coding:

.. edify-playground::

   from edify.library import encoding

   encoding("gzip")     # registered
   encoding("utf-8")    # a charset: see charset
   encoding("lzma")     # not a registered coding
   encoding("gzip;q=")  # no quality value

This matches one coding at a time. A full ``Accept-Encoding`` header may list several
comma-separated values — split on commas first.
