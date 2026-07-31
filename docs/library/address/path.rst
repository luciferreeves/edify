Path
====

**Path** recognises three families of filesystem path —
`POSIX <https://en.wikipedia.org/wiki/Path_(computing)#POSIX_pathname_definition>`__,
Windows, and `UNC <https://en.wikipedia.org/wiki/Path_(computing)#UNC>`__ — and is
deliberately permissive within each: it matches the *shape* of a path, not whether the
file exists. The only string it rejects outright is the empty one.

The three families are the branches of an :func:`~edify.any_of`, and each segment is a
:meth:`~edify.RegexBuilder.one_or_more` run of
:meth:`~edify.RegexBuilder.anything_but_chars` — "any character except the forbidden
few". POSIX forbids the null byte, carriage return, newline, and ``/``; Windows and
UNC additionally forbid the characters illegal in a filename (``\`` ``/`` ``:`` ``*``
``?`` ``"`` ``<`` ``>`` ``|``).

POSIX paths
-----------

An optional ``/``, ``./``, or ``../`` prefix, then slash-separated segments —
absolute, relative, or parent-relative to any depth. Spaces and most punctuation are
fine inside a segment:

.. edify-playground::

   from edify.library import path

   path("/usr/local/bin")               # absolute
   path("relative/dir")                 # relative
   path("./config.yaml")                # dot-relative
   path("../../up/two")                 # parent-relative
   path("my documents/report v2.txt")   # spaces are allowed

Windows and UNC paths
---------------------

A drive letter with backslash segments, or a ``\\server\share`` UNC path:

.. edify-playground::

   from edify.library import path

   path("C:\\Windows\\System32")    # drive path
   path("D:\\data\\file.txt")       # another drive path
   path("\\\\server\\share")        # UNC share
   path("\\\\nas\\media\\movies")   # a deeper UNC path

Because it is so permissive, **Path** won't distinguish a real path from arbitrary
slashed text — reach for it when you want the shape, not strict validation.
